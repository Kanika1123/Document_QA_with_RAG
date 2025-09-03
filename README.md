Resume link: https://drive.google.com/file/d/1hKCMavdNGI2s5oQ8RxhkespBwuaqEAWs/view?usp=sharing

# Document_QA_with_RAG

🚀 **Live Demo:** [Click here to try the app](https://documentappwithrag-nj3xvnlmdg69ewvkcktrea.streamlit.app/)


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
2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
3. Install Dependencies
   pip install -r requirements.txt
   (If requirements.txt is missing, install manually:)
   pip install streamlit faiss-cpu sentence-transformers
4.Run the app
   streamlit run rag_app.py

   
Example Usage
Upload tech.txt or any text file.

Ask a question like "What is cloud computing?".
The app retrieves the most relevant chunks and produces a final answer.

Future Improvements:
- Add support for PDF and DOCX files.  
- Integrate a generative LLM for more natural answers.  
- Experiment with smarter semantic chunking (sentence/paragraph-based splits).  
- Auto-tune chunk size based on document length for better retrieval.  

 Author
Kanika Bansal
   
   
   

   
