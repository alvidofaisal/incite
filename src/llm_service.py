import os
from typing import AsyncGenerator
from groq import Groq

class LLMService:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = os.getenv("LLM_MODEL", "llama3-8b-8192")
        
    async def generate_response(
        self,
        query: str,
        context: str 
    ) -> AsyncGenerator[str, None]:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": f"Question: {query}\nContext: {context}" # Query is the user's question, Context is the search results
            }
        ]
        
        stream = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
