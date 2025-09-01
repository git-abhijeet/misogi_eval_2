
from pydantic import EmailStr, BaseModel, Field
from datetime import datetime
from typing import Optional


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    phone_number: str
    balance: float

class CreateUser(User):
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class UpdateUser(BaseModel):
    username: Optional[str]
    phone_number: Optional[str]