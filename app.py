import os
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    # Initialize RAGSearch
    # It will automatically load documents from 'data' folder and build the FAISS index if it doesn't exist
    rag_search = RAGSearch()
    
    print("\nRAG System Initialized! Type 'exit' or 'quit' to stop.")
    while True:
        query = input("\n[USER] Enter your question: ").strip()
        if query.lower() in ['exit', 'quit']:
            break
        if not query:
            continue
            
        print(f"\n[INFO] Searching for: '{query}'")
        summary = rag_search.search_and_summarize(query, top_k=3)
        print(f"\n[SUMMARY]\n{summary}")

