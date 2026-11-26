
"""
NovaMind - AI Document Assistant
Main backend application
"""

from fastapi import FastAPI

app = FastAPI(
    title="NovaMind",
    description="An AI-powered document assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "NovaMind",
        "status": "running",
        "message": "Welcome to NovaMind!"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
