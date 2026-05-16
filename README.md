# AI Research Assistant (RAG-Based Multi-PDF Question Answering System)

A research assistant application that enables users to upload research papers and interact with them through intelligent question answering, summarization, semantic search, and quiz generation.

The system processes uploaded PDF documents, retrieves relevant contextual information, and generates accurate responses based on the uploaded content.

---

# Overview

The AI Research Assistant allows users to:

- Upload one or multiple PDF research papers
- Extract and process document text
- Perform semantic search across uploaded documents
- Ask natural language questions from research papers
- Generate research summaries
- Create quizzes automatically from uploaded content
- Download generated answers
- Explore retrieved contextual chunks

The application combines document retrieval techniques with language models to improve answer quality using uploaded research content.

---

# Features

## Document Processing
- Multi-PDF upload support
- Automated text extraction from PDFs
- Intelligent text chunking for efficient retrieval

## Question Answering
- Context-aware responses from uploaded documents
- Semantic similarity search using vector embeddings
- Multiple response styles:
  - Simple
  - Detailed
  - Research-focused

## Research Assistance
- Research paper summarization
- Automatic quiz generation from uploaded papers
- Downloadable answer generation

## User Experience
- Interactive Streamlit interface
- Chat history support
- Retrieved context viewer
- Loading spinners for improved experience
- Sidebar navigation

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application framework |
| LangChain | Application workflow orchestration |
| FAISS | Vector database for semantic retrieval |
| HuggingFace Embeddings | Text embedding generation |
| Groq LLM | Language model inference |
| PyPDF | PDF text extraction |
| dotenv | Environment variable management |

---

# System Architecture

```text
PDF Upload
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Store
    ↓
Semantic Retrieval
    ↓
Response Generation
```

---

# Project Workflow

1. User uploads one or more PDF research papers.
2. The application extracts text from uploaded documents.
3. Extracted text is divided into chunks for efficient processing.
4. Embeddings convert text chunks into vector representations.
5. FAISS stores embeddings for semantic similarity search.
6. User asks questions in natural language.
7. Relevant chunks are retrieved using vector similarity.
8. Responses are generated using retrieved document context.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/rag-research-assistant.git
```

## Navigate to Project Directory

```bash
cd rag-research-assistant
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows
```bash
venv\Scripts\activate
```

### Linux / macOS
```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Running the Application

```bash
streamlit run main.py
```

The application will launch locally in your browser.

---

# Example Use Cases

- Academic research assistance
- Literature review support
- Research paper understanding
- Study material summarization
- Scientific document exploration
- Automated quiz generation
- Knowledge extraction from PDFs

---

# Sample Capabilities

## Ask Questions
- "What methodology is used in this paper?"
- "Explain the findings in simple language."
- "What are the limitations of this research?"

## Generate Summary
Produces:
- Main topic
- Methodology
- Key findings
- Conclusion
- Limitations

## Generate Quiz
Creates multiple-choice questions directly from uploaded research papers.

---

# Current Features Implemented

- Multi-document retrieval pipeline
- Semantic search using embeddings
- Vector retrieval using FAISS
- Research summarization
- Quiz generation
- Downloadable outputs
- Interactive Streamlit interface
- Chat history support

---

# Future Improvements

- Conversational memory
- Citation generation
- PDF highlighting
- Research paper comparison
- Voice input support
- Cloud deployment
- Persistent vector database

---

# Screenshots

## Home Interface
![Home](assets/home)

## Question Answering
![Answer](assets/Q&A)

## Research Summary
![Summary](assets/summary)

## Quiz Generation
![Quiz](assets/Quiz1)
![Quiz](assets/Quiz2)

---

# Learning Outcomes

This project demonstrates practical understanding of:

- Semantic Search
- Vector Databases
- Embedding Models
- Retrieval Pipelines
- Prompt Engineering
- Streamlit Application Development
- End-to-End Document Processing Workflows

---

# Author

Shuchi Tiwari

---

# License

This project is developed for educational, research, and portfolio purposes.
