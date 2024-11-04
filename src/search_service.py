import os
import httpx    
from typing import Dict, Any

class SearchService:
    """Handles search operations using the Serper API for Google search results"""
    def __init__(self):
        # Initialize with API credentials and endpoint
        self.api_key = os.getenv("SERPER_API_KEY")
        self.base_url = "https://google.serper.dev/search"
        self.headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json',
        }
        
    async def search(self, query: str, location: str = 'us') -> Dict[str, Any]:
        """
        Performs an async search request to Serper API
        Returns: Dictionary containing search results
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.base_url,
                headers=self.headers,
                json={
                    "q": query,      # Search query
                    "num": 20,       # Number of results to return
                    "gl": location   # Geographic location for search context
                }
            )
        return response.json()