
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from ai_engine import AIEngine

app = FastAPI(
    title="NovaMind",
    description="AI Document Assistant",
    version="1.0.0"
)

ai = AIEngine()


class ChatRequest(BaseModel):
    question: str


@app.get("/api/health")
def health():
    return {"status": "healthy"}


@app.post("/chat")
def chat(request: ChatRequest):
    answer = ai.generate_response(request.question)
    return {"answer": answer}


frontend_path = (
    Path(__file__).resolve().parent.parent / "frontend"
)

app.mount(
    "/",
    StaticFiles(directory=str(frontend_path), html=True),
    name="frontend"
)
