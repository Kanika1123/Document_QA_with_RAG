import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline

# -------------------------------
# Helper: Split text into chunks
# -------------------------------
def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Document Q&A with RAG", layout="wide")

st.title("Document Q&A with RAG")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    st.success("File uploaded successfully!")
    st.text_area("File content preview", text[:500])

    # -------------------------------
    # Chunking
    # -------------------------------
    chunks = chunk_text(text, chunk_size=300, overlap=50)
    st.write(f"📖 Split into {len(chunks)} chunks")

    # -------------------------------
    # Embeddings
    # -------------------------------
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks, convert_to_numpy=True)

    # -------------------------------
    # FAISS Index
    # -------------------------------
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    st.success("FAISS index built")

    # -------------------------------
    # User Question
    # -------------------------------
    query = st.text_input("Ask a question:")
    k = st.slider("Number of chunks to retrieve (k)", 1, 5, 3)

    if query:
        query_embedding = model.encode([query], convert_to_numpy=True)
        distances, indices = index.search(query_embedding, k)

        st.subheader("Top Retrieved Chunks")
        retrieved_chunks = []
        for i, idx in enumerate(indices[0]):
            retrieved_chunks.append(chunks[idx])
            st.write(f"{i+1}. {chunks[idx][:300]}...")

        # -------------------------------
        # Use QA Pipeline
        # -------------------------------
        qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

        context = " ".join(retrieved_chunks)
        result = qa_pipeline(question=query, context=context)

        st.subheader("Final Answer")
        st.write(result["answer"])
