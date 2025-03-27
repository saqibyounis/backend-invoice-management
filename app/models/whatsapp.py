from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from .base import Base

class WhatsAppMessage(Base):
    __tablename__ = "whatsapp_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(String, default="sent")  # sent, delivered, failed
    created_at = Column(DateTime, nullable=False)
    phone_number = Column(String, nullable=False)

    user = relationship("User", back_populates="whatsapp_messages")