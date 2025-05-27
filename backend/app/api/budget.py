from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.openai_budget_estimator import estimate_budget_items

router = APIRouter()

class BudgetItem(BaseModel):
    item: str
    quantity: int

class BudgetRequest(BaseModel):
    project_title: str
    items: List[BudgetItem]

@router.post("/estimate-budget")
async def estimate_budget(request: BudgetRequest):
    try:
        result = estimate_budget_items(request.project_title, request.items)
        return {"budget_estimate": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
