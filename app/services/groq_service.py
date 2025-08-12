import groq
from groq import Groq
from app.core.config import settings
from fastapi import HTTPException

class GroqService:
    def __init__(self, client=None):
        self.client = client or Groq(api_key=settings.GROQ_API_KEY)
        self.default_model = settings.GROQ_DEFAULT_MODEL 

    async def generate_response(self, prompt: str, model: str = None) -> str:
        try:
            if not prompt.strip():
                raise ValueError("A pergunta não pode estar vazia")
            
            model = model or self.default_model

            messages = [
                {
                    "role": "system",
                    "content": "Você é um assistente de vendas especializado em produtos para pets. Sempre que possível, sugira produtos presentes no site da petlove: https://www.petlove.com.br"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]

            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=model,
                temperature=0.5,
                max_tokens=1024  
            )
            
            return chat_completion.choices[0].message.content
            
        except groq.APIConnectionError as e:
            raise HTTPException(
                status_code=503,
                detail=f"Erro de conexão com a Groq: {str(e)}"
            )
        except groq.APIError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Erro na API da Groq: {str(e)}"
            )

# Instância pronta para uso
groq_service = GroqService()