from typing import Optional
from enum import Enum
from pydantic import BaseModel, EmailStr, constr
import uuid


class UserRole(str, Enum):
    user = 'user'
    admin = 'admin'


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: constr(min_length=10, max_length=15)
    password: constr(min_length=8)
    role: Optional[UserRole] = UserRole.user


class UserResponse(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    role: UserRole

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'