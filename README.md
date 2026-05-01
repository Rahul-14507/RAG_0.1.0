# RAG-Tutorials

This project implements a basic Retrieval-Augmented Generation (RAG) system for question answering using LangChain, Groq LLM, and FAISS vector store.

## Prerequisites

- Python 3.8+
- Java (required by FAISS)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/RAG-Tutorials.git
   cd RAG-Tutorials
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install langchain langchain-community langchain-text-splitters langchain-google-genai faiss-cpu sentence-transformers tiktoken pypdf
   ```

4. Create a `.env` file in the project root and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_API_KEY=your_langsmith_api_key
   LANGSMITH_ENDPOINT=https://api.smith.langchain.com
   LANGSMITH_PROJECT=your-project-name
   ```

## Usage

### 1. Load Documents and Build Index

The system automatically builds the FAISS index from documents in the `data/` directory when needed.

```bash
# Run the application (will build index if not exists)
python app.py
```

### 2. Build Index Manually

You can also build the index manually:

```bash
python src/data_loader.py
```

### 3. Query the System

```bash
python app.py

# Or specify a different model
python app.py --model gemma2-9b-it
```

### Command-Line Options

```bash
python app.py --help

Usage: app.py [OPTIONS] [QUERY]

Arguments:
  QUERY  The question to ask

Options:
  --top-k INTEGER                 Number of documents to retrieve [default: 5]
  --model TEXT                    LLM model to use [default: gemma2-9b-it]
  --help                          Show this message and exit.
```

## Project Structure

```
RAG-Tutorials/
├── data/                   # Source documents
│   ├── embedding_explanation.txt
│   └── attention_mechanism.txt
├── faiss_store/            # Built FAISS index (created automatically)
├── src/
│   ├── data_loader.py      # Loads documents and builds FAISS index
│   ├── embedding_store.py  # FAISS vector store implementation
│   ├── search.py           # RAG search and summarization
│   └── utils.py            # Utility functions
├── app.py                  # Main application entry point
└── requirements.txt        # Project dependencies
```

## How It Works

1. **Data Loading**: `src/data_loader.py` scans the `data/` directory for `.txt` files.
2. **Embedding**: It uses `sentence-transformers` (all-MiniLM-L6-v2) to convert document chunks into vector embeddings.
3. **Indexing**: The embeddings are stored in a FAISS index for efficient similarity search.
4. **Retrieval**: When a query is made, `src/search.py` finds the most similar document chunks using FAISS.
5. **Generation**: The retrieved context is passed to Groq LLM (default: `gemma2-9b-it`) to generate a summary/answer.

## Testing

Run the unit tests:

```bash
python -m unittest tests/test_embedding_store.py
python -m unittest tests/test_data_loader.py
```
