from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.services.groq_service import groq_service

router = APIRouter()

@router.get("/health")
async def health_check():
    return JSONResponse(
        content={"status": "OK", "message": "Works"},
        status_code=200
    )

@router.post("/question-and-answer")
async def question_answer(question: str):
    try:
        prompt = (
            "Como assistente de vendas especializado em produtos para pets, "
            f"responda esta pergunta de forma clara e útil: {question}\n"
            "Dê recomendações específicas de produtos PETLOV quando possível."
        )
        
        response = await groq_service.generate_response(prompt)
        return {"response": response}
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno: {str(e)}"
        )