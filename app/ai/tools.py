from typing import Dict


def get_customer(phone: str) -> Dict:
    return {
        "phone": phone,
        "name": "Customer",
    }


def get_conversation_history(phone: str) -> list:
    return []


def save_ai_message(phone: str, message: str) -> Dict:
    return {
        "phone": phone,
        "message": message,
        "status": "saved",
    }


def send_ai_reply(phone: str, message: str) -> Dict:
    return {
        "phone": phone,
        "message": message,
        "status": "sent",
    }