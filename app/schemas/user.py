from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr #TODO: Need to replace emailstr with phone.
    is_active: bool = True

class UserCreate(UserBase):
    password: str  # Only for user creation

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True