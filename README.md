
# rag-qa-hr-faq

# RAG-Based QA System for HR FAQs

This project implements a basic Retrieval-Augmented Generation (RAG) pipeline to answer employee questions using a small HR FAQ knowledge base.



## Objective

Build a question-answering system that:
- Retrieves relevant FAQ entries from a knowledge base using sentence embeddings/HuggingFaceEmbeddings
- Uses a language model (LLM) to generate responses based on retrieved context.
- Follows the RAG pattern for combining search + generation.



## Architecture

text
User Question
     ↓
Sentence Embedding (query)
     ↓
FAISS Vector Search (Top-k relevant chunks)
     ↓
Prompt Construction
     ↓
LLM Generation (using Hugging Face Mistral / or any other Hugging Face models)
     ↓
Final Answer


# HR FAQ Assistant - RAG-based Question Answering system

# Features
. Retrieval-Augmented Generation (RAG) pipeline
. FAISS vector store with Sentence Transformers
. Custom prompt template enforcing grounded answers
. Fallback response if answer is not in context
. Streamlit interface for interactive Q&A
. Evaluation metrics on question coverag(optional    bonus)

# Tech Stack
Embedding Model: sentence-transformers/all-MiniLM-L6-v2
Vector Store: FAISS
LLM: Qwen/Qwen1.5-0.5B-Chat via Hugging Face Transformers
RAG Logic: LangChain + PromptTemplate
UI: Streamlit
Evaluation: JSON + Notebook (optional)

# How it Works
1.	Preprocessing: HR FAQs are cleaned, chunked, and embedded.
2.	Storage: Embeddings are stored in FAISS for similarity search.
3.	RAG Flow:
- A user question is embedded and matched with top-k documents.
- Retrieved context is passed into a prompt with the question.
- A language model generates an answer grounded in context.
4. Fallback Logic: If no relevant info is found, the assistant replies with:
'I don't know. I couldn’t find information about this. You might try rephrasing your question.'

# Streamlit UI
activate venv:
    venv/Scripts/activate (on windows)
To run the app:
    python -m streamlit run app/streamlit_app.py


# Evaluation (Optional)
 Evaluation summary is saved to qa_evaluation.json and which is in development.ipynb  

# Requirements
     pip install requirements.txt 

