from pydantic import BaseModel
from datetime import datetime

class InvoiceBase(BaseModel):
    user_id: int
    amount: float
    status: str = "pending"

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceResponse(InvoiceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True