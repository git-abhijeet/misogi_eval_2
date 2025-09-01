from fastapi import HTTPException
from controllers.transfer_controllers import transfer_money
from schemas.transfer_schemas import TransferRequest


async def transfer_money_handler(transfer_request: TransferRequest):
    try:
        print("🐍 [transfer_handler.py:7] ▶", transfer_request)
        # Logic for transferring money
        transaction = await transfer_money(transfer_request)
        # pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return transaction