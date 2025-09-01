
from pydantic import EmailStr, BaseModel, Field
from datetime import datetime
from typing import Optional

class Wallet(BaseModel):
    user_id: str
    balance: float
    last_updated: datetime

class WalletTransaction(BaseModel):
    amount: float
    description: str
