# 🧠 PalChat

A powerful AI assistant chat application built with **FastAPI**, **LangChain**, **OpenAI GPT-4o**, and **FAISS**, enabling Retrieval-Augmented Generation (RAG), JWT & Google OAuth2 authentication, user sessions, and secure document uploads.

---

## ✨ Features

- 🔐 JWT authentication (Signup & Signin)
- 🔑 Google OAuth2 login
- 👥 Role-based access control (User, Admin)
- 📁 PDF, TXT, and Markdown file upload for RAG
- 💬 Persistent chat sessions (with history)
- 📚 FAISS + LangChain document retrieval
- 🧠 GPT-4o-powered conversational AI
- ✅ Modular FastAPI project structure

---

## 🗂️ Project Structure

```

app/
├── core/
│ ├── chat\_engine.py \# Handles RAG chat logic
│ ├── document\_loader.py \# Splits and loads PDFs/TXT
│ ├── vector\_engine.py \# Retrieval from FAISS
│ └── vector\_store.py \# Creates and saves FAISS index
├── crud/
│ └── user.py \# User DB operations
├── dependencies/
│ ├── auth.py \# Auth token validation
│ └── roles.py \# Role-based permissions
├── models/
│ ├── chat.py \# ChatMessage & ChatSession models
│ └── user.py \# User model with role support
├── routes/
│ ├── chat.py \# Chat endpoints
│ ├── upload.py \# File upload endpoints
│ ├── user.py \# Signup / Signin endpoints
│ └── google\_oauth.py \# Google OAuth2 login
├── schemas/
│ ├── chat.py \# Chat request/response schemas
│ └── user.py \# User models & auth schemas
├── utils/
│ └── security.py \# Hashing, JWT functions
├── database.py \# SQLAlchemy DB connection
└── main.py \# FastAPI app entrypoint

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/genaichat.git](https://github.com/your-username/genaichat.git)
cd genaichat
````

### 2\. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3\. Install dependencies

```bash
pip install -r requirements.txt
```

### 4\. Add environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_jwt_secret_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
DATABASE_URL=postgresql://user:password@localhost/genaichat
```

### 5\. Run migrations

```bash
alembic upgrade head
```

### 6\. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

-----

## 🔐 Auth & Permissions

### JWT Authentication

| Endpoint        | Method | Description          |
|-----------------|--------|----------------------|
| `/auth/signup`  | `POST`   | Create new account   |
| `/auth/signin`  | `POST`   | Login & get token    |

Use the `Bearer` token in the `Authorization` header to access protected routes.

### Google OAuth2

| Endpoint               | Description       |
|------------------------|-------------------|
| `/auth/google/`        | Redirect to Google |
| `/auth/google/callback` | OAuth2 token + user |

### Roles

  - **user**: Default role for regular users
  - **admin**: For admin-only access (extendable)

Middleware checks user roles on protected routes.

-----

## 🧠 Chat + RAG

| Endpoint                 | Method   | Description             |
|--------------------------|----------|-------------------------|
| `/api/v1/chat/new-session` | `POST`     | Creates new chat session |
| `/api/v1/chat/`          | `POST`     | Chat using RAG context  |
| `/api/v1/chat/{session_id}` | `DELETE`   | Delete session          |
| `/api/v1/chat/{session_id}/history` | `GET`      | Get chat history        |

### How it works

1.  User uploads a document
2.  System splits into chunks
3.  Chunks embedded using OpenAI
4.  Stored in FAISS index
5.  During chat, relevant chunks retrieved using similarity search
6.  Prompt is composed with context + query
7.  GPT-4o generates contextual answer

-----

## 📁 File Upload (RAG Input)

| Endpoint        | Method | Description                      |
|-----------------|--------|----------------------------------|
| `/api/v1/upload/` | `POST`   | Upload PDF/TXT/MD for vector DB |

Only supported formats: `.pdf`, `.txt`, `.md`

-----

## 🧪 Testing the API

  * Visit `http://localhost:8000/docs` for Swagger UI
  * Use Postman to test OAuth2 callback (Swagger does not support Google login redirect)

-----

## 🗝️ Technologies Used

  * FastAPI
  * LangChain
  * OpenAI GPT-4o
  * FAISS
  * Authlib
  * SQLAlchemy + Alembic
  * PostgreSQL

-----

## ✅ Future Enhancements

  * Refresh tokens
  * Email verification
  * Admin dashboard
  * Web frontend (React / Next.js)
  * File indexing by user
  * Logging + analytics

-----

## 📜 License

This project is licensed under the MIT License.

-----

## 🙌 Author

Built with ❤️ by Ifeoluwa Ilori.

```
```