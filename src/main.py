from typing import Optional
from fastapi.responses import StreamingResponse
import orjson as json
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from llm_service import LLMService
from search_service import SearchService
from content_processor import ContentProcessor

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Incite",
    description="Open-source AI search engine.",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
llm_service = LLMService()
search_service = SearchService()
content_processor = ContentProcessor()
@app.get("/")
async def root():
    return {"message": "Welcome to Incite API!"}

# Basic liveness
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/search")
async def search(
    q: str = Query(..., description="Search query"),
    num: Optional[int] = Query(
        default=10,
        description="Number of results",
        ge=1,
        le=20,  
    ),
    gl: Optional[str] = Query(
        default="us",
        description="Geographic location"
    )
):
    """
    Streaming search endpoint that returns both search results and LLM-processed responses
    """
    # Get search results
    results = await search_service.search(query=q, location=gl)
    
    # Prepare context for LLM from search results
    context = content_processor.process_search_results(results)
    
    async def generate_stream():
        # Send search results first
        yield f"data: {json.dumps({
            'type': 'search_results', # Indicates the type of data being sent, e.g. search results/LLM response
            'data': results # The actual search results
        }).decode()}\n\n"
        
        # Stream LLM response
        async for chunk in llm_service.generate_response(q, context):
            yield f"data: {json.dumps({
                'type': 'llm_response',
                'data': chunk
            })}"
            
        yield "data: {\"type\": \"done\"}\n\n"
        
    return StreamingResponse(
        generate_stream(),  # First argument: async generator function
        media_type="text/event-stream"
    )
        