from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health")
async def health_check():
    return JSONResponse(
        content={"status": "OK", "message": "Works"},
        status_code=200
    )