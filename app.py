import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="SmartDoc AI", layout="wide")

st.title("📄 SmartDoc AI - RAG Chatbot")
st.write("Upload PDFs and chat with them 🤖")

# -----------------------------
# Chat Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Upload PDFs
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload PDF files",
    type="pdf",
    accept_multiple_files=True
)

# -----------------------------
# Stop if no file
# -----------------------------
if not uploaded_files:
    st.info("👆 Upload at least one PDF to start")
    st.stop()

# -----------------------------
# Load Local LLM (cached)
# -----------------------------
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

pipe = load_model()

def local_llm(prompt):
    result = pipe(prompt, max_length=200, do_sample=False)
    return result[0]["generated_text"]

# -----------------------------
# Process PDFs
# -----------------------------
all_docs = []

for file in uploaded_files:
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", file.name)

    with open(file_path, "wb") as f:
        f.write(file.read())

    loader = PyPDFLoader(file_path)
    documents = loader.load()
    all_docs.extend(documents)

# -----------------------------
# Split Text
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = splitter.split_documents(all_docs)

# -----------------------------
# Embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# -----------------------------
# Vector Store
# -----------------------------
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# -----------------------------
# CHAT UI 🔥
# -----------------------------
st.subheader("💬 Chat with your PDF")

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
query = st.chat_input("Ask something about your PDF...")

if query:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):

            # Retrieve relevant docs
            retrieved_docs = retriever.invoke(query)
            context = "\n\n".join([doc.page_content for doc in retrieved_docs])

            # Prompt
            final_prompt = f"""
            Answer based only on the context below:

            Context:
            {context}

            Question: {query}
            """

            # Generate answer
            answer = local_llm(final_prompt)

            st.markdown(answer)

    # Store assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})

    # Optional: Show sources
    with st.expander("📚 Source Context"):
        st.write(context)
