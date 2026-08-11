from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import SessionLocal
from database.models import Message
from schemas.message import WebhookMessage, MessageResponse
from app.ai.graph import graph

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/webhook", response_model=MessageResponse)
def webhook(
    message: WebhookMessage,
    db: Session = Depends(get_db)
):
    try:
        if message.location:
            message_content = f"Location received: latitude={message.location.latitude}, longitude={message.location.longitude}"
        elif message.contact:
            message_content = f"Contact received: name={message.contact.name}, phone={message.contact.phone}"
        else:
            message_content = message.content

        new_message = Message(
            sender=message.sender,
            receiver=message.receiver,
            content=message_content,
            status="delivered"
        )

        db.add(new_message)
        db.commit()
        db.refresh(new_message)

        history_messages = db.query(Message).filter(
            (Message.sender == message.sender) |
            (Message.receiver == message.sender)
        ).order_by(Message.id).all()

        history = [msg.content for msg in history_messages]

        ai_result = graph.invoke({
            "phone": message.sender,
            "message": message_content,
            "intent": "",
            "response": "",
            "history": history
        })

        ai_reply = Message(
            sender=message.receiver,
            receiver=message.sender,
            content=ai_result.get("response", ""),
            status="delivered"
        )

        db.add(ai_reply)
        db.commit()
        db.refresh(ai_reply)

        return ai_reply

    except Exception as e:
        db.rollback()
        print("WEBHOOK ERROR:", repr(e))
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )