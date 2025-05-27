from fastapi import FastAPI
from dotenv import load_dotenv
from app.api import rfp

load_dotenv()

app = FastAPI()

app.include_router(rfp.router)

@app.get("/")
def root():
    return {"message": "Smart Tender AI API is live!"}
