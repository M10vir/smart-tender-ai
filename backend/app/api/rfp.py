from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.openai_rfp_generator import generate_rfp_from_objectives

router = APIRouter()

class RFPRequest(BaseModel):
    tender_title: str
    project_objectives: str

@router.post("/generate-rfp")
async def generate_rfp(request: RFPRequest):
    try:
        result = generate_rfp_from_objectives(request.tender_title, request.project_objectives)
        return {"generated_rfp": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
