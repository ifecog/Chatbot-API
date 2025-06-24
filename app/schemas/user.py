from pydantic import BaseModel, EmailStr, constr
import uuid


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: constr(min_length=10, max_length=15)
    password: constr(min_length=8)


class UserResponse(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str

    class Config:
        orm_mode = True
