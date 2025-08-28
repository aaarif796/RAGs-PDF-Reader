# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 15:47:12 2025

@author: AnsariMohammad
"""

import os
import tempfile
from typing import List, Dict, Any
from dotenv import load_dotenv, find_dotenv

# LangChain imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

class PDFChatbot:
    def __init__(self):
        """Initialize the PDF Chatbot"""
        # Load environment variables
        load_dotenv(find_dotenv())
        self.api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
        
        if not self.api_token:
            raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables")
        
        # Initialize components
        self.llm = None
        self.embeddings = None
        self.vectordb = None
        self.rag_chain = None
        self.chat_history = []
        self.is_initialized = False
        
        # Setup LLM and embeddings
        self._setup_models()
    
    def _setup_models(self):
        """Setup LLM and embedding models"""
        try:
            # Initialize LLM
            self.llm = ChatOpenAI(
                temperature=0.0,
                model="openai/gpt-oss-120b",
                base_url="https://router.huggingface.co/v1",
                api_key=self.api_token,
            )
            
            # Initialize embeddings
            self.embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2",
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )
            
            print("Models initialized successfully")
            
        except Exception as e:
            print(f"Error initializing models: {e}")
            raise
    
    def load_pdf(self, pdf_file_path: str) -> Dict[str, Any]:
        """Load and process PDF file"""
        try:
            # Load PDF
            loader = PyPDFLoader(pdf_file_path)
            docs = loader.load()
            
            if not docs:
                return {"success": False, "message": "No content found in PDF"}
            
            # Split into chunks
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
                is_separator_regex=False,
            )
            chunks = splitter.split_documents(docs)
            
            # Create vector database
            persist_directory = "chroma_db_temp"
            self.vectordb = Chroma.from_documents(
                documents=chunks,
                embedding=self.embeddings,
                persist_directory=persist_directory
            )
            
            # Setup RAG chain
            self._setup_rag_chain()
            
            self.is_initialized = True
            self.chat_history = []  # Reset chat history for new PDF
            
            return {
                "success": True,
                "message": f"PDF loaded successfully! Found {len(docs)} pages and created {len(chunks)} chunks.",
                "pages": len(docs),
                "chunks": len(chunks)
            }
            
        except Exception as e:
            return {"success": False, "message": f"Error loading PDF: {str(e)}"}
    
    def _setup_rag_chain(self):
        """Setup the RAG chain for question answering"""
        system_prompt = (
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know. Keep the answer concise and helpful."
            "\n\n"
            "{context}"
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        # Create document chain
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        
        # Create retrieval chain
        retriever = self.vectordb.as_retriever(search_kwargs={"k": 3})
        self.rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    def ask_question(self, question: str) -> Dict[str, Any]:
        """Ask a question about the loaded PDF"""
        if not self.is_initialized:
            return {"success": False, "answer": "Please load a PDF first."}
        
        try:
            # Get response from RAG chain
            result = self.rag_chain.invoke({"input": question})
            answer = result["answer"]
            
            # Update chat history
            self.chat_history.append({
                "question": question,
                "answer": answer
            })
            
            return {
                "success": True,
                "answer": answer,
                "sources": len(result.get("context", []))
            }
            
        except Exception as e:
            return {"success": False, "answer": f"Error processing question: {str(e)}"}
    
    def get_chat_history(self) -> List[Dict[str, str]]:
        """Get the current chat history"""
        return self.chat_history
    
    def clear_history(self):
        """Clear the chat history"""
        self.chat_history = []
    
    def is_ready(self) -> bool:
        """Check if the chatbot is ready to answer questions"""
        return self.is_initialized
