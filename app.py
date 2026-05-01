import os
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    # Initialize RAGSearch
    # It will automatically load documents from 'data' folder and build the FAISS index if it doesn't exist
    rag_search = RAGSearch()
    
    query = "What is attention mechanism?"
    print(f"\n[QUERY] {query}")
    
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("\n[SUMMARY]\n", summary)
