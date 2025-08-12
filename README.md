### AI Assistant API — Integração com Groq

API para integração com o **Groq**, permitindo processar requisições e fornecer respostas inteligentes para um assistente de e-commerce.  
Desenvolvido em **Python** com **FastAPI**, testes automatizados com **pytest** e cobertura configurada.

---

## 🚀 Funcionalidades

- Integração com API Groq para respostas inteligentes.
- Endpoints REST desenvolvidos com **FastAPI**.
- Estrutura modular e escalável.
- Testes automatizados com **pytest**.
- Suporte a variáveis de ambiente via arquivo `.env`.

---

## 📦 Requisitos

- **Python** 3.10 ou superior
- Conta e **API Key** do [Groq](https://groq.com/)
- Pip (gerenciador de pacotes)

---

## ⚙️ Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/AnabelCristina/ai_assistant.git
   cd ai_assistant
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `.env`**

   Crie um arquivo `.env` na raiz do projeto com:
   ```env
   GROQ_API_KEY=sua_chave_aqui
   ```

---

## ▶️ Execução

Para iniciar o servidor local:

```bash
uvicorn main:app --reload
```

A API ficará disponível em:
```
http://127.0.0.1:8000
```

Documentação interativa (Swagger):
```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testes

Para rodar os testes:

```bash
pytest -v
```


