from groq import Groq
from dotenv import load_dotenv
import pytest

from app.core.config import settings
load_dotenv()

async def test_real_groq_connection():
    client = Groq(api_key=settings.GROQ_API_KEY)
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": "Teste de conexão"}],
            model="llama3-70b-8192"
        )
        assert len(chat_completion.choices[0].message.content) > 0
    except Exception as e:
        pytest.fail(f"Falha na conexão com Groq: {str(e)}")