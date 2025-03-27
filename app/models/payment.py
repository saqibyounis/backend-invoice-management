from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")  # e.g., pending, completed, failed
    payment_method = Column(String, nullable=False)  # e.g., credit_card, paypal, bank_transfer
    transaction_id = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime, nullable=False)

    invoice = relationship("Invoice", back_populates="payments")