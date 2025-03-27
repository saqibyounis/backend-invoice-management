from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    invoice_id: int
    amount: float
    status: str
    payment_method: str

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int
    transaction_id: str | None
    created_at: datetime

    class Config:
        from_attributes = True