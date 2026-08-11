from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import Base, engine
from database.models import Message
from routes.messages import router as messages_router
from routes.webhook import router as webhook_router


Base.metadata.create_all(bind=engine)


app = FastAPI(title="WhatsApp Business API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(messages_router)
app.include_router(webhook_router)

