# to run in terminal:
# uvicorn copykitt_api:app --reload

from fastapi import FastAPI, HTTPException
from copykitt import generate_branding_snippet, generate_keywords

app = FastAPI()
MAX_INPUT_LENGTH = 32

@app.get("/")
async def root():
    return {"message": "Hello CopyKitt"}

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str): 
    validate_length_api(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []} 

@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str): 
    validate_length_api(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords} 

@app.get("/generate_snippet_and_keywords")
async def generate_snippet_and_keywords_api(prompt: str): 
    validate_length_api(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords} 

def validate_length_api(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail=f"Input length too long. Must be under {MAX_INPUT_LENGTH} characters.")

    pass