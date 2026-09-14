from datetime import datetime

from pydantic import BaseModel


class QuestionResponse(BaseModel):
    yourQuistion: str
    response: str


class QuestionRequest(BaseModel):
    question: str


class UserRequest(BaseModel):
    firstname: str
    lastname: str
    email: str
    hashed_password: str
    created_at: datetime


# login
class LoginRequest(BaseModel):
    email: str
    password: str


class SignupResponse(BaseModel):
    message: str
    user: dict


# ── Message ──────────────────────────────────────────
class MessageCreate(BaseModel):
    content: str
    # image_url: Optional[File] = None


class MessageOut(BaseModel):
    id: str
    role: str  # "user" | "assistant"
    content: str
    image_url: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


# ── Chat Session ─────────────────────────────────────
class ChatSessionCreate(BaseModel):
    title: str | None = None  # if None, auto-generate from first message


class ChatSessionOut(BaseModel):
    id: str
    title: str | None
    created_at: datetime
    messages: list[MessageOut] = []

    model_config = {"from_attributes": True}
