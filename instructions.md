# Building Incite Backend

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

## API Keys Required

The following API keys are needed:
- Cohere API
- JINA AI API
- Serper.dev API (for Google search)
- Groq API

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YassKhazzan/openperplex_backend_os.git
   cd openperplex_backend_os
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   
   Create a `.env` file in the root directory:
   ```env
   COHERE_API_KEY=your_cohere_key
   JINA_API_KEY=your_jina_key
   SERPER_API_KEY=your_serper_key
   GROQ_API_KEY=your_groq_key
   ```

## Running the Application

### Local Development
```bash
uvicorn main:app --port 8000
```
Access at `http://localhost:8000`

### Docker Deployment

1. **Build the Docker Image**
   ```bash
   docker build -t openperplex-backend .
   ```

2. **Run the Container**
   ```bash
   docker run -p 8080:8080 --env-file .env openperplex-backend
   ```
Access at `http://localhost:8080`

## API Endpoints

### Health Checks
- `GET /` - Basic health check
- `GET /up_test` - Deployment test endpoint

### Search
- `GET /search`
  - Parameters:
    - `query`: Search query string
    - `date_context`: Date context for search
    - `stored_location`: Location for search results
    - `pro_mode`: Enable advanced features (default: false)

## Core Features

### 1. Semantic Chunking
- Uses Cohere for intelligent text chunking
- Splits text into meaningful segments

### 2. Search Results Processing
- Google search integration via serper.dev
- Structured result processing

### 3. Content Reranking
- JINA and Cohere reranking support
- Improves search result relevancy

### 4. LLM Integration
- Groq API with Llama 3 70B model
- AI-powered responses

## Error Handling
- Comprehensive error logging
- Client-appropriate error responses

## Development Notes
- CORS enabled for all origins in development
- Default ports:
  - Local development: 8000
  - Docker deployment: 8080
- Docker optimized for OVH Cloud AI Deploy

## License
MIT License

# TODO

## 1. Update Search Endpoint
- Change POST to GET for `/search` endpoint
- Add required parameters:
  - `date_context`
  - `stored_location` 
  - `pro_mode`
Reference:

## 2. Enhance LLM Service
- Update system prompt
- Add date context support
- Add relevant questions generation
Reference:

## 3. Improve Content Processing
- Add support for multiple result types:
  - Organic results
  - Top stories
  - Knowledge graph
  - Answer box
- Implement HTML content extraction
Reference:

## 4. Add Reranking Support
- Implement JINA reranking
- Add Cohere reranking as fallback
Reference:

## 5. Enhance Search Service
- Add pro_mode support
- Implement field extraction
- Add error handling
Reference:

## 6. Update Dependencies
Add to requirements.txt:
- semantic-chunkers==0.0.9
- semantic-router==0.0.55
- cohere==5.6.2
- langchain-core==0.2.27

## 7. Environment Variables
Add to .env:
```env
COHERE_API_KEY=your_key
JINA_API_KEY=your_key
SERPER_API_KEY=your_key
GROQ_API_KEY=your_key
LLM_MODEL=llama3-70b-8192
```

## 8. Implementation Order
1. Update search endpoint parameters
2. Implement enhanced content processing
3. Add reranking support
4. Update LLM service
5. Add pro mode features
6. Implement error handling

## 9. Testing Requirements
- Test each reranking provider
- Verify pro mode functionality
- Test HTML content extraction
- Validate streaming responses
- Check error handling

## 10. Notes
- Keep existing CORS configuration
- Maintain async/await pattern
- Use proper error handling
- Follow existing logging format

## 11. Documentation Updates
- Update API documentation
- Add new parameter descriptions
- Document pro mode features
- Include reranking options



