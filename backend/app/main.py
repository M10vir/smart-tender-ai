from fastapi import FastAPI
from dotenv import load_dotenv
from app.api import rfp, budget, scoring

load_dotenv()

app = FastAPI()

app.include_router(rfp.router)
app.include_router(budget.router)
app.include_router(scoring.router)

@app.get("/")
def root():
    return {"message": "Smart Tender AI API is live!"}
