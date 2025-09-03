Resume link: https://drive.google.com/file/d/1hKCMavdNGI2s5oQ8RxhkespBwuaqEAWs/view?usp=sharing

# Document Q&A with RAG

This project is a lightweight implementation of **Retrieval-Augmented Generation (RAG)** for answering questions from documents.  
It combines **embeddings** (MiniLM) with a **vector store (FAISS)** to retrieve relevant text chunks and generate answers.



##  Project Structure
- `rag_app.py` – the main Streamlit app
- `tech.txt` – document with technology-related content (ML, DL, Cloud, Full Stack)
- `ai.txt` – document with AI-related content
- `blockchain.txt` – document with blockchain-related content
- `README.md` – project documentation



##  Features
- Upload any `.txt` document.
- Text is **split into chunks** for better retrieval.
- FAISS index is built from embeddings.
- Ask natural language questions about the document.
- Adjustable number of chunks (`k`) to tune retrieval.
- Simple Streamlit interface.



## 🔧 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Kanika1123/Document_QA_with_RAG.git
   cd Document_QA_with_RAG
