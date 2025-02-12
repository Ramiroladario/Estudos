responses = {
    "oi": "Olá! Como posso te ajudar?",
    "qual é o seu nome?": "Eu sou um chatbot simples!",
    "como você está?": "Eu sou um programa, mas estou funcionando bem! 😃",
    "adeus": "Tchau! Tenha um ótimo dia!",
}

def get_response(message: str) -> str:
    message = message.lower()
    return responses.get(message, "Desculpe, não entendi. Pode reformular?")
