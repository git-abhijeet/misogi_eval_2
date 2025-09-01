from fastapi import HTTPException
from controllers.wallet_controller import get_balance, add_balance, withdraw_balance
# from schemas.user_schemas import User, CreateUser, UpdateUser
from schemas.wallet_schemas import WalletTransaction


async def get_balance_handler(user_id: str):
    # Logic to get the user's wallet balance    
    try:
        user_balance = await get_balance(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_balance
    


async def add_balance_handler(user_id: str, data: WalletTransaction):
    # Logic to add balance to the user's wallet
        try:
            user_transaction = await add_balance(user_id, data)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        return user_transaction

async def withdraw_balance_handler(user_id: str, data: WalletTransaction):
    # Logic to withdraw balance from the user's wallet
        try:
            user_transaction = await withdraw_balance(user_id, data)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        return user_transaction
