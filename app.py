# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 15:45:24 2025

@author: AnsariMohammad
"""


import streamlit as st
import tempfile
import os
from pdf_chatbot import PDFChatbot

# Page configuration
st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .bot-message {
        background-color: #f1f8e9;
        border-left: 4px solid #4caf50;
    }
    .stButton > button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = None
    if 'pdf_loaded' not in st.session_state:
        st.session_state.pdf_loaded = False
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def display_chat_history():
    """Display chat history with newest entries first"""
    history = st.session_state.chatbot.get_chat_history()[::-1]  # reverse list
    if history:
        st.subheader("💬 Chat History")
        for chat in history:
            # User message
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {chat['question']}
            </div>
            """, unsafe_allow_html=True)

            # Bot message
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>Assistant:</strong> {chat['answer']}
            </div>
            """, unsafe_allow_html=True)


def main():
    """Main Streamlit app"""
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">📚 PDF Chatbot</h1>', unsafe_allow_html=True)
    st.markdown("Upload a PDF and ask questions about its content!")
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Controls")
        
        # File upload
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type="pdf",
            help="Upload a PDF file to analyze"
        )
        
        # Initialize chatbot button
        if st.button("🤖 Initialize Chatbot"):
            try:
                with st.spinner("Initializing chatbot..."):
                    st.session_state.chatbot = PDFChatbot()
                st.success("Chatbot initialized successfully!")
            except Exception as e:
                st.error(f"Error initializing chatbot: {str(e)}")
        
        # Load PDF button
        if uploaded_file and st.session_state.chatbot:
            if st.button("📄 Load PDF"):
                with st.spinner("Processing PDF..."):
                    # Save uploaded file temporarily
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                        tmp_file.write(uploaded_file.read())
                        tmp_file_path = tmp_file.name
                    
                    # Load PDF
                    result = st.session_state.chatbot.load_pdf(tmp_file_path)
                    
                    # Clean up temp file
                    os.unlink(tmp_file_path)
                    
                    if result["success"]:
                        st.success(result["message"])
                        st.session_state.pdf_loaded = True
                    else:
                        st.error(result["message"])
        
        # Clear history button
        if st.session_state.chatbot and st.session_state.chatbot.is_ready():
            if st.button("🗑️ Clear History"):
                st.session_state.chatbot.clear_history()
                st.success("Chat history cleared!")
                st.rerun()
        
        # Status
        st.header("📊 Status")
        if st.session_state.chatbot:
            st.success("✅ Chatbot initialized")
            if st.session_state.chatbot.is_ready():
                st.success("✅ PDF loaded and ready")
            else:
                st.warning("⚠️ Please load a PDF")
        else:
            st.warning("⚠️ Please initialize chatbot")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Chat interface
        if st.session_state.chatbot and st.session_state.chatbot.is_ready():
            st.subheader("💭 Ask a Question")
            
            # Question input
            question = st.text_area(
                "Enter your question about the PDF:",
                height=100,
                placeholder="What is this document about?"
            )
            
            # Ask button
            if st.button("🚀 Ask Question", type="primary"):
                if question.strip():
                    with st.spinner("Thinking..."):
                        result = st.session_state.chatbot.ask_question(question)
                    
                    if result["success"]:
                        st.success("Question answered!")
                        st.rerun()  # Refresh to show new chat history
                    else:
                        st.error(result["answer"])
                else:
                    st.warning("Please enter a question!")
            
            # Display chat history
            display_chat_history()
        
        else:
            st.info("👆 Please initialize the chatbot and load a PDF to start chatting!")
    
    with col2:
        # Instructions
        st.subheader("📋 Instructions")
        st.markdown("""
        1. **Initialize**: Click 'Initialize Chatbot' first
        2. **Upload**: Choose a PDF file from your computer
        3. **Load**: Click 'Load PDF' to process the document
        4. **Chat**: Ask questions about the PDF content
        5. **Clear**: Use 'Clear History' to start fresh
        """)
        
        # Tips
        st.subheader("💡 Tips")
        st.markdown("""
        - Ask specific questions for better answers
        - Questions about document content work best
        - The chatbot remembers previous questions
        - Processing may take a moment for large PDFs
        """)

if __name__ == "__main__":
    main()
