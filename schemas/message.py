from enum import Enum
from pydantic import BaseModel, Field


class MessageStatus(str, Enum):
    sent = "sent"
    delivered = "delivered"
    read = "read"

class MessageCreate(BaseModel):
    sender: str = Field(min_length=10, max_length=15)
    receiver: str = Field(min_length=10, max_length=15)
    content: str = Field(min_length=1, max_length=4096)
    status: MessageStatus = MessageStatus.sent

class LocationData(BaseModel):
    latitude: float
    longitude: float

class ContactData(BaseModel):
    name: str = ""
    phone: str = ""

class WebhookMessage(BaseModel):
    sender: str = Field(min_length=10, max_length=15)
    receiver: str = Field(min_length=10, max_length=15)
    content: str = ""
    location: LocationData | None = None
    contact: ContactData | None = None

class MessageResponse(BaseModel):
    id: int
    sender: str
    receiver: str
    content: str
    status: str

    class Config:
        from_attributes = True
