from pydantic import BaseModel
from datetime import datetime

class WhatsAppMessageBase(BaseModel):
    user_id: int
    message: str
    phone_number: str
    status: str = "sent"

class WhatsAppMessageCreate(WhatsAppMessageBase):
    pass

class WhatsAppMessageResponse(WhatsAppMessageBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = Truey