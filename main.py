import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

load_dotenv()

# Page Config
st.set_page_config(page_title="AI Research Assistant")

# Sidebar
with st.sidebar:

    st.title("AI Research Assistant")

    st.write("Upload PDFs and ask questions.")

    st.write("Built using:")
    st.write("- Streamlit")
    st.write("- FAISS")
    st.write("- HuggingFace Embeddings")
    st.write("- Groq LLM")

# Main Title
st.title("AI Research Assistant")
st.write("Upload research paper PDFs and ask questions.")

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload PDFs
pdf_docs = st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

# Process PDFs
if pdf_docs:

    with st.spinner("Reading PDFs..."):

        text = ""

        for pdf in pdf_docs:

            pdf_reader = PdfReader(pdf)

            for page in pdf_reader.pages:

                extracted_text = page.extract_text()

                if extracted_text:
                    text += extracted_text

    # Text Splitter
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_text(text)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector Database
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # LLM
    llm = ChatGroq(
        model_name="llama-3.1-8b-instant"
    )

    # Response Style
    mode = st.selectbox(
        "Choose Response Style",
        ["Simple", "Detailed", "Research"]
    )

    # Summary Button
    if st.button("Generate Summary"):

        with st.spinner("Generating Summary..."):

            summary_prompt = f"""
            Summarize this research paper simply.

            Include:
            - main topic
            - methodology
            - findings
            - conclusion
            - limitations

            Text:
            {text[:12000]}
            """

            summary_response = llm.invoke(summary_prompt)

            st.subheader("Research Summary")
            st.write(summary_response.content)

    # Quiz Button
    if st.button("Generate Quiz"):

        with st.spinner("Generating Quiz..."):

            quiz_prompt = f"""
            Create 10 MCQs from this research paper.

            Text:
            {text[:10000]}
            """

            quiz_response = llm.invoke(quiz_prompt)

            st.subheader("Quiz")
            st.write(quiz_response.content)

    # User Question
    user_question = st.text_input(
        "Ask a question from the PDF"
    )

    if user_question:

        with st.spinner("Generating Answer..."):

            # Similarity Search
            docs = knowledge_base.similarity_search(
                user_question
            )

            # Build Context
            context = "\n".join(
                [doc.page_content for doc in docs]
            )

            # Prompt
            prompt = f"""
            You are an AI research assistant.

            Response style: {mode}

            First answer using PDF context.
            Then optionally use general knowledge.

            Context:
            {context}

            Question:
            {user_question}

            Answer:
            """

            # Generate Response
            response = llm.invoke(prompt)

            # Save Chat
            st.session_state.chat_history.append(
                {
                    "question": user_question,
                    "answer": response.content
                }
            )

            # Display Chats
            st.subheader("Chat History")

            for chat in st.session_state.chat_history:

                st.markdown("### Question")
                st.write(chat["question"])

                st.markdown("### Answer")
                st.write(chat["answer"])

            # Retrieved Chunks
            with st.expander("View Retrieved Context"):

                for i, doc in enumerate(docs):

                    st.write(f"Chunk {i+1}")
                    st.write(doc.page_content)
                    st.write("------")

            # Download Answer
            st.download_button(
                label="Download Answer",
                data=response.content,
                file_name="answer.txt",
                mime="text/plain"
            )