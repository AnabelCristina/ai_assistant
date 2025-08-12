from app.services.groq_service import GroqService
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

@pytest.fixture
def mock_groq():
    mock = AsyncMock()
    mock.chat.completions.create.return_value = {
        "choices": [{"message": {"content": "service answer"}}]
    }
    return mock

@pytest.mark.asyncio
async def test_generate_response_success():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="resposta teste"))]
    )
    
    service = GroqService(client=mock_client)
    response = await service.generate_response("teste") 
    
    assert response == "resposta teste"


@pytest.mark.asyncio
async def test_empty_prompt():
    service = GroqService() 
    with pytest.raises(ValueError, match="A pergunta não pode estar vazia"):
        await service.generate_response("")
