def ask_atlas(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! I am Atlas AI, your business assistant. How can I help you?"

    elif "price" in message or "cost" in message:
        return "I can help with pricing questions. Please tell me what service you are interested in."

    else:
        return "Thank you for your message. I am Atlas AI and I will help you with your request."
