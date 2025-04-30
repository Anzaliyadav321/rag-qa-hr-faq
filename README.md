# rag-qa-hr-faq

# RAG-Based QA System for HR FAQs

This project implements a basic Retrieval-Augmented Generation (RAG) pipeline to answer employee questions using a small HR FAQ knowledge base.

---

## Objective

Build a question-answering system that:
- Retrieves relevant FAQ entries from a knowledge base using sentence embeddings/HuggingFaceEmbeddings
- Uses a language model (LLM) to generate responses based on retrieved context.
- Follows the RAG pattern for combining search + generation.

---

## Architecture

'''text
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
Final Answer'''
