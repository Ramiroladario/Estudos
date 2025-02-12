from chatbot.chatbot_logic import get_response

def test_get_response():
    assert get_response("oi") == "Olá! Como posso te ajudar?"
    assert get_response("qual é o seu nome?") == "Eu sou um chatbot simples!"
    assert get_response("desconhecido") == "Desculpe, não entendi. Pode reformular?"
    assert get_response("adeus") == "Tchau! Tenha um ótimo dia!"