from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import SessionLocal
from database.models import Message
from schemas.message import MessageCreate, MessageResponse, MessageStatus
from services.whatsapp import send_whatsapp_message


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/messages", response_model=list[MessageResponse])
def get_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()

@router.get(
    "/messages/{phone}",
    response_model=list[MessageResponse]
)
def get_messages_by_phone(
    phone: str,
    db: Session = Depends(get_db)
):
    messages = db.query(Message).filter(
        (Message.sender == phone) | (Message.receiver == phone)
    ).all()

    if not messages:
        raise HTTPException(
            status_code=404,
            detail="No messages found for this phone number"
        )

    return messages

@router.post("/send-message", response_model=MessageResponse)
async def send_message(
    message: MessageCreate,
    db: Session = Depends(get_db)
):
    try:
        response = await send_whatsapp_message(
            message.receiver,
            message.content
        )

        if not response.get("success"):
            raise HTTPException(
                status_code=502,
                detail="WhatsApp message sending failed"
            )

        new_message = Message(
            sender=message.sender,
            receiver=message.receiver,
            content=message.content,
            status=message.status
        )

        db.add(new_message)
        db.commit()
        db.refresh(new_message)

        return new_message

    except HTTPException:
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to send message"
        )
@router.patch("/messages/{message_id}/status")
def update_message_status(
    message_id: int,
    status: MessageStatus,
    db: Session = Depends(get_db)
):
    message = db.query(Message).filter(
        Message.id == message_id
    ).first()

    if not message:
        raise HTTPException(
            status_code=404,
            detail="Message not found"
        )

    message.status = status.value
    db.commit()
    db.refresh(message)

    return message