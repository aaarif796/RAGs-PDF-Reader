# RAGs-PDF-Reader 📚🤖

A powerful **Retrieval-Augmented Generation (RAG)** application that allows you to chat with your PDF documents using state-of-the-art language models. Upload any PDF and ask questions about its content through an intuitive Streamlit web interface.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/🦜🔗_LangChain-blue)

## ✨ Features

- 📄 **PDF Upload & Processing**: Load any PDF document through the web interface
- 🧠 **Advanced RAG Pipeline**: Uses OpenAI's GPT-OSS models via Hugging Face router
- 💬 **Interactive Chat Interface**: Ask questions and get intelligent answers about your PDF content
- 📚 **Document Chunking**: Efficiently splits large documents into manageable chunks
- 🔍 **Semantic Search**: Uses sentence-transformers for accurate content retrieval
- 💾 **Vector Storage**: ChromaDB for persistent embedding storage
- 🕒 **Chat History**: Maintains conversation context across multiple questions
- 🎨 **Beautiful UI**: Clean and responsive Streamlit interface
- ⚡ **Real-time Processing**: Fast document processing and question answering

## 🚀 Complete Installation Guide

### Prerequisites

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **Git** ([Download Git](https://git-scm.com/downloads))
- **Hugging Face API Token** ([Get one here](https://huggingface.co/settings/tokens))

### Step 1: Check System Requirements

First, verify your Python installation:

```bash
python --version
# or
python3 --version
```

You should see Python 3.8+ (e.g., "Python 3.9.7" or "Python 3.11.2")

### Step 2: Download the Project

#### Option A: Using Git (Recommended)
```bash
git clone https://github.com/aaarif796/RAGs-PDF-Reader.git
cd RAGs-PDF-Reader
```

#### Option B: Download ZIP
1. Go to [GitHub Repository](https://github.com/aaarif796/RAGs-PDF-Reader)
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Navigate to the extracted folder

### Step 3: Create Virtual Environment

#### For Windows:
```cmd
# Create virtual environment
python -m venv gen_ai

# Activate virtual environment
gen_ai\Scripts\activate

# Verify activation (you should see (gen_ai) in your prompt)
```

#### For macOS/Linux:
```bash
# Create virtual environment
python3 -m venv gen_ai

# Activate virtual environment
source gen_ai/bin/activate

# Verify activation (you should see (gen_ai) in your prompt)
```

#### Using Anaconda (Alternative):
```bash
# Create conda environment
conda create -n gen_ai python=3.9 -y

# Activate environment
conda activate gen_ai
```

### Step 4: Install Dependencies

#### Method 1: Using requirements.txt (Recommended)
```bash
# Make sure your virtual environment is activated
pip install -r requirements.txt
```

#### Method 2: Manual Installation
If you encounter issues with requirements.txt, install packages individually:

```bash
# Core packages
pip install streamlit==1.28.0
pip install langchain
pip install langchain-community
pip install langchain-chroma
pip install langchain-huggingface
pip install langchain-openai
pip install langchain-text-splitters

# Supporting packages
pip install chromadb
pip install sentence-transformers
pip install torch
pip install pypdf
pip install python-dotenv
pip install openai
```

### Step 5: Set Up Environment Variables

#### Method 1: Create .env file
Create a file named `.env` in the project root directory:

```env
HUGGINGFACEHUB_API_TOKEN=your_actual_token_here
```

**To get your Hugging Face token:**
1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Click "New token"
3. Give it a name (e.g., "RAG-PDF-Reader")
4. Select "Read" permissions
5. Copy the generated token

#### Method 2: Set Environment Variable Directly

**Windows (Command Prompt):**
```cmd
set HUGGINGFACEHUB_API_TOKEN=your_actual_token_here
```

**Windows (PowerShell):**
```powershell
$env:HUGGINGFACEHUB_API_TOKEN="your_actual_token_here"
```

**macOS/Linux:**
```bash
export HUGGINGFACEHUB_API_TOKEN="your_actual_token_here"
```

### Step 6: Verify Installation

Test if everything is installed correctly:

```bash
python -c "import streamlit, langchain, chromadb; print('All packages installed successfully!')"
```

### Step 7: Run the Application

```bash
# Make sure you're in the project directory and virtual environment is activated
streamlit run app.py
```

**Expected Output:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.1.xxx:8501
```

### Step 8: Use the Application

1. **Open your browser** and go to `http://localhost:8501`
2. **Click "🤖 Initialize Chatbot"** (wait for success message)
3. **Upload a PDF file** using the file uploader
4. **Click "📄 Load PDF"** (wait for processing to complete)
5. **Ask questions** about your PDF in the text area
6. **Click "🚀 Ask Question"** to get answers

## 🛠️ Troubleshooting Installation Issues

### Common Problems and Solutions

#### Problem 1: Python Command Not Found
```bash
# Try these alternatives:
python3 --version
py --version
python3.9 --version
```

#### Problem 2: Permission Errors (Windows)
```cmd
# Run as administrator or use:
python -m pip install --user -r requirements.txt
```

#### Problem 3: Virtual Environment Issues
```bash
# Deactivate current environment
deactivate

# Remove old environment
rm -rf gen_ai  # Linux/Mac
rmdir /s gen_ai  # Windows

# Create new environment
python -m venv gen_ai_new
```

#### Problem 4: Package Installation Failures
```bash
# Upgrade pip first
pip install --upgrade pip

# Install packages one by one
pip install streamlit
pip install langchain
# ... continue with others
```

#### Problem 5: ChromaDB Issues
```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install build-essential

# For macOS
xcode-select --install

# Alternative: Use SQLite backend
pip install chromadb[sqlite]
```

#### Problem 6: Token Issues
```bash
# Check if token is set
python -c "import os; print(os.environ.get('HUGGINGFACEHUB_API_TOKEN', 'Token not found'))"

# Test token validity
python -c "from huggingface_hub import HfApi; api = HfApi(); print('Token valid!' if api.whoami() else 'Invalid token')"
```

### Memory Requirements

- **Minimum RAM**: 8GB
- **Recommended RAM**: 16GB+
- **Storage**: 2GB free space (for model downloads)

### Port Issues

If port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

## 🔄 Updating the Project

To get the latest version:

```bash
# Navigate to project directory
cd RAGs-PDF-Reader

# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade
```

## 🗂️ Project Structure

```
RAGs-PDF-Reader/
├── app.py                 # Main Streamlit application
├── pdf_chatbot.py        # Core chatbot class implementation
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── README.md            # This file
├── chroma_db_temp/      # ChromaDB storage (auto-created)
└── gen_ai/             # Virtual environment (auto-created)
```

## 💻 System-Specific Instructions

### Windows Users
- Use `python` instead of `python3`
- Use backslashes `\` in paths
- Consider using PowerShell instead of Command Prompt
- May need Visual Studio Build Tools for some packages

### macOS Users
- May need to install Xcode Command Line Tools
- Use `python3` explicitly
- Homebrew can help with system dependencies:
  ```bash
  brew install python
  ```

### Linux Users
- Install system dependencies:
  ```bash
  sudo apt-get update
  sudo apt-get install python3-pip python3-venv build-essential
  ```
- Use `python3` and `pip3` explicitly

### Docker Alternative (Advanced)

For consistent environments across all systems:

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

```bash
# Build and run
docker build -t rag-pdf-reader .
docker run -p 8501:8501 -e HUGGINGFACEHUB_API_TOKEN=your_token rag-pdf-reader
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the RAG framework
- [Streamlit](https://streamlit.io/) for the web interface
- [Hugging Face](https://huggingface.co/) for model hosting and APIs
- [OpenAI](https://openai.com/) for the GPT-OSS models
- [ChromaDB](https://www.trychroma.com/) for vector storage

---

**Made with ❤️ by [aaarif796](https://github.com/aaarif796)**

*If this project helped you, please consider giving it a ⭐!*

