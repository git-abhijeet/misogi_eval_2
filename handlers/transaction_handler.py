from fastapi import HTTPException, Query
from controllers.transaction_controller import user_transaction, transaction_detail



async def get_user_transactions_handler(user_id: str, page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100)):
    try:
        transaction = await user_transaction(user_id, page, limit)
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
    return transaction

async def get_transaction_detail_handler(transaction_id: str):
    try:
        transaction = await transaction_detail(transaction_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return transaction
