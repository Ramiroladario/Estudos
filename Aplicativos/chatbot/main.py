from fastapi import FastAPI
from chatbot.chatbot_logic import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bem-vindo ao 2kbot API!"}

@app.get("/chatbot/")
def chatbot(message: str):
    response = get_response(message)
    return {"user_message": message, "chatbot_response": response}
