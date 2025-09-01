from pydantic import EmailStr, BaseModel, Field
from datetime import datetime
from typing import Optional


class TransferRequest(BaseModel):
    sender_user_id: str
    recipient_user_id: str
    amount: float
    description: Optional[str]

