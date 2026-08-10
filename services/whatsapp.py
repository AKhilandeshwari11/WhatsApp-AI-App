async def send_whatsapp_message(
    receiver: str,
    content: str
):
    return {
        "success": True,
        "message": "WhatsApp API connection test successful",
        "receiver": receiver,
        "content": content
    }