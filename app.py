from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chatbot import generate_response
from database import create_table
from database import save_chat
from database import get_all_chats

app = FastAPI(title="AI Chatbot API")

create_table()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Chatbot API Running"}


@app.post("/chat")
def chat(data: UserMessage):

    user_msg = data.message

    bot_reply = generate_response(user_msg)

    save_chat(user_msg, bot_reply)

    return {
        "user_message": user_msg,
        "bot_response": bot_reply
    }


@app.get("/history")
def history():

    chats = get_all_chats()

    return {
        "chat_history": chats
    }
