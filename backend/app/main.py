from fastapi import FastAPI
from dotenv import load_dotenv
from app.api import rfp, budget

load_dotenv()

app = FastAPI()

app.include_router(rfp.router)
app.include_router(budget.router)

@app.get("/")
def root():
    return {"message": "Smart Tender AI API is live!"}
