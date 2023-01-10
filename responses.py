import random

def generate_response(input_msg: str) -> str:
    input_msg = input_msg.lower()
    if input_msg == '!hi':
        return "Hello there!"
    elif input_msg == '!how are you?':
        return "I am fine."
    elif input_msg == "!help":
        return "Welcome to my bot. Currently supported commands are: '!hi', '!how are you?' and '!help'. \n This bot is in development"
    else:
        return "Message not understood. Run '!help' to see the supported commands."