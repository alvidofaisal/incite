import os
from typing import List
from semantic_chunkers import StatisticalChunker
from semantic_router.encoders import CohereEncoder

class ContentProcessor:
    def __init__(self):
        self.encoder = CohereEncoder(
            cohere_api_key=os.getenv("COHERE_API_KEY"),
            input_type='search_document',
            name='embed-multilingual-v3.0'
        )
        self.chunker = StatisticalChunker(
            encoder=self.encoder,
            max_split_tokens=200,
        )
    
    def process_search_results(self, results: dict) -> str:
        """
        Process and chunk search results into a format suitable for LLM context
        """
        # Step 1: Get organic search results
        organic_results = results.get('organic', [])
        
        # Step 2: Format each result
        context_parts = []
        for idx, result in enumerate(organic_results, 1):
            part = (
                f"[{idx}] Title: {result.get('title', '')}\n"
                f"Snippet: {result.get('snippet', '')}\n"
                f"Link: {result.get('link', '')}\n"
            )
            context_parts.append(part)
        
        # Step 3: Combine and chunk
        full_context = "\n".join(context_parts)
        chunks = self.chunk_text(full_context)
        
        # Step 4: Return first 3 chunks
        return "\n".join(chunks[:3])

    def chunk_text(self, text: str) -> List[str]:
        """
        Split text into semantic chunks
        """
        try:
            # Try to chunk text
            chunks = self.chunker(docs=[text])
        except Exception as e:
            # If chunking fails, return the entire text as a single chunk
            print(f"Error in chunking text: {e}")
            return [text]
            
