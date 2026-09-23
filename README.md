# 🤖 AI-EGENT

> **Open Source Deep Research AI Agent** — Powered by LangChain, FastAPI & Free AI APIs

An intelligent, open-source AI project designed to help you build AI applications using entirely free services like the **Groq API**. It provides pre-made, production-ready APIs so you can easily build chat apps similar to ChatGPT or Claude. Features include question-answering, multi-turn chat sessions, user history tracking, image understanding, and deep research capabilities — all backed by a PostgreSQL database.

---

## ✨ Features

| Feature | Status |
|---|---|
| 🧠 AI Q&A (question & answer routes) | ✅ Done |
| 👤 User Authentication (JWT) | 🔧 In Progress |
| 🗂️ Chat Session & History System | 🔧 In Progress |
| 🖼️ Image Understanding & Explanation | 🔧 In Progress |
| 🐘 PostgreSQL Database (via SQLAlchemy + Alembic) | ✅ Configured |
| 🔄 Database Migrations (Alembic) | ✅ Configured |

---

## 🗂️ Project Structure

```
AI-EGENT/
├── main.py               # FastAPI app entry point
├── personal.py           # Personal/dev utilities
├── alembic.ini           # Alembic migration config
├── requirements.txt      # Python dependencies
├── alembic/              # Database migration scripts
├── src/
│   ├── config/
│   │   └── db.py         # Database engine & session setup
│   ├── schemas/
│   │   └── schema.py     # SQLAlchemy models (User, ChatSession, Message)
│   └── routes/
│       ├── ai_router.py  # AI question & answer endpoints
│       └── userRoute.py  # User management endpoints
└── pymodule/             # Custom Python modules
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/Nahid625/AI-EGENT.git
cd AI-EGENT
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/ai_egent
SECRET_KEY=your_secret_key_here
GROQ_API_KEY=your_groq_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 4. Run Database Migrations

```bash
alembic upgrade head
```

### 5. Start the Server

```bash
python main.py
```

The API will be available at `http://127.0.0.1:8000`

---

## 📡 API Endpoints

### AI Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/AI/question` | Ask a simple text question without session |
| `POST` | `/AI/ask` | Ask with text and optional image, starts a session |
| `POST` | `/AI/ask/{session_id}` | Ask a follow-up question in an existing session |

### User Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/user/signup` | Register a new user |
| `POST` | `/user/login` | Login and get JWT token |

### Chat Session Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/chat/sessions` | Create a new chat session explicitly |
| `GET`  | `/chat/sessions` | List all chat sessions for the user |
| `GET`  | `/chat/sessions/{id}`| Get a session with its full message history |
| `DELETE`| `/chat/sessions/{id}`| Delete a specific session |

---

## 🗺️ Roadmap

- [x] AI Q&A route implementation
- [x] PostgreSQL integration with SQLAlchemy
- [x] Alembic migration setup
- [x] **Auth system** — JWT-based user registration & login
- [x] **Chat history system** — Persist and retrieve per-user Q&A history
- [x] **Image understanding** — Allow users to upload images and get AI explanations (via Cloudinary)
- [x] **Session management** — Create, retrieve, and delete chat sessions
- [ ] Pagination for chat histories
- [ ] Rate limiting & API key management
- [ ] Dockerize the application

---

## 🛠️ Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **AI / LLM:** [LangChain](https://www.langchain.com/) & Free APIs (e.g., [Groq](https://groq.com/))
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
- **Server:** [Uvicorn](https://www.uvicorn.org/)

---

## 🤝 Contributing & Development Workflow

To maintain a clean Git history and continuous integration, we follow a strict Pull Request (PR) workflow for every change.

### Development Process
1. **Create a new branch** for your task:
   `git checkout -b feature/your-feature-name` (or `fix/...`, `docs/...`)
2. **Make your changes** and test them locally.
3. **Commit your changes**:
   `git add .`
   `git commit -m "feat: your descriptive message"`
4. **Push the branch** to GitHub:
   `git push -u origin feature/your-feature-name`
5. **Create a Pull Request** using GitHub CLI:
   `gh pr create --fill`
6. **Merge the Pull Request** (this will auto-merge and delete the branch):
   `gh pr merge --merge --delete-branch`
7. **Clean up locally**:
   `git checkout main`
   `git pull origin main`
   `git branch -D feature/your-feature-name`

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 👤 Author

**Nahid** — [@Nahid625](https://github.com/Nahid625)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).