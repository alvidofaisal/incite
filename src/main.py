from typing import Optional
import orjson as json
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from search_service import SearchService

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

@app.get("/")
async def root():
    return {"message": "Welcome to Incite API!"}

# Basic liveness
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Search Service
search_service = SearchService()

@app.post("/search")
async def search(
    q: str = Query(..., description="Search query"),
    num: Optional[int] = Query(
        default=20,
        description="Number of results",
        
        
    )
    
)

