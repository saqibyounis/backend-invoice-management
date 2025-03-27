from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.base import SessionLocal
from app.models.whatsapp import WhatsAppMessage
from app.schemas.whatsapp import WhatsAppMessageCreate, WhatsAppMessageResponse
from datetime import datetime

router = APIRouter(prefix="/whatsapp", tags=["WhatsApp"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Send a WhatsApp message (store in DB)
@router.post("/", response_model=WhatsAppMessageResponse)
def send_whatsapp_message(message_data: WhatsAppMessageCreate, db: Session = Depends(get_db)):
    message = WhatsAppMessage(**message_data.dict(), created_at=datetime.utcnow())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

# Get message by ID
@router.get("/{message_id}", response_model=WhatsAppMessageResponse)
def get_whatsapp_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(WhatsAppMessage).filter(WhatsAppMessage.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

# Get all messages
@router.get("/", response_model=list[WhatsAppMessageResponse])
def get_whatsapp_messages(db: Session = Depends(get_db)):
    return db.query(WhatsAppMessage).all()