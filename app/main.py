from fastapi import FastAPI
from app.api import user, invoice, payment, whatsapp

app = FastAPI(title="Invoice Management API")

app.include_router(user.router)
app.include_router(invoice.router)
app.include_router(payment.router)
app.include_router(whatsapp.router)

@app.get("/")
def home():
    return {"message": "Welcome to Invoice Management API"}