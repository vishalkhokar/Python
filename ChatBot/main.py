import time
import streamlit as st
from app.pdf_read import readPddf
from app.embedding import create_emdeding,retrive_relevant_docs
from app.chatmodel import get_chat_model,ask_chat_model
from app.config import EURI_API_KEY
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(
    page_title="Railway enquiry - Railway Assistant",
    page_icon="🚄",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #2b313e;
        color: white;
    }
    .chat-message.assistant {
        background-color: #f0f2f6;
        color: black;
    }
    .chat-message .avatar {
        width: 2rem;
        height: 2rem;
        border-radius: 50%;
        margin-right: 0.5rem;
    }
    .chat-message .message {
        flex: 1;
    }
    .chat-message .timestamp {
        font-size: 0.8rem;
        opacity: 0.7;
        margin-top: 0.5rem;
    }
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 0.5rem;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #ff3333;
    }
    .upload-section {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .status-success {
        background-color: #d4edda;
        color: #155724;
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "chat_model" not in st.session_state:
    st.session_state.chat_model = None
    

all_texts=[]
for text in readPddf():
    all_texts.append(text)
    
#print(all_texts)

textspilter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    length_function=len
)
    
chunks=[]
for text in all_texts:
    chunks.extend(textspilter.split_text(text))

print(chunks)


vectorstore=create_emdeding(chunks)
st.session_state.vectorstore = vectorstore

chat_model=get_chat_model(EURI_API_KEY)
st.session_state.chat_model=chat_model

st.markdown("### 💬 Chat with Your Railway Enquiry")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        st.caption(message["timestamp"])

# Chat input
if prompt := st.chat_input("Ask about your Railway..."):
    # Add user message to chat history
    timestamp = time.strftime("%H:%M")
    st.session_state.messages.append({
        "role": "user", 
        "content": prompt, 
        "timestamp": timestamp
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(timestamp)
    
    # Generate response
    if st.session_state.vectorstore and st.session_state.chat_model:
        with st.chat_message("assistant"):
                relevant_docs = retrive_relevant_docs(st.session_state.vectorstore, prompt)
                
                # Create context from relevant documents
                context = "\n\n".join([doc.page_content for doc in relevant_docs])
                
                # Create prompt with context
                system_prompt = f"""You are Railway enquiry Pro, an Railway enquiry assistant. 
                Based on the following Railway question , provide accurate and helpful answers. 
                If the information is not in the documents, clearly state that.

                Railway:
                {context}

                User Question: {prompt}

                Answer:"""
                
                response = ask_chat_model(st.session_state.chat_model, system_prompt)
            
                st.markdown(response)
                st.caption(timestamp)
                
                message=[]                
            # Add assistant message to chat history
                st.session_state.messages.append({
                "role": "assistant", 
                "content": response, 
                "timestamp": timestamp
            })

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>🏥 Railway Enquiry Intelligence</p>
</div>
""", unsafe_allow_html=True)    
