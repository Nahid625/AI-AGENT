# main.py
from fastapi import FastAPI

from src.config.db import Base, engine
from src.routes.chat_router import router as ChatRouter
from src.schemas.schema import ChatSession, Message, User

Base.metadata.create_all(bind=engine)

from src.routes.ai_router import router as aiRouter
from src.routes.userRoute import router as UserRouter

app = FastAPI(title="Ai learning")

routes = [aiRouter, UserRouter, ChatRouter]
for r in routes:
    app.include_router(r)

if __name__ == "__main__":
    import os

    import uvicorn

    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
