from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.vendor_scorer import score_vendor_proposal

router = APIRouter()

@router.post("/score-vendor")
async def score_vendor(file: UploadFile = File(...)):
    try:
        result = score_vendor_proposal(file)
        return {"score_report": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
