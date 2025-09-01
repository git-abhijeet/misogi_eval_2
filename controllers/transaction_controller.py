from config.db import user_collection, transaction_collection
from bson.objectid import ObjectId
from fastapi import HTTPException
from datetime import datetime


async def user_transaction(user_id: str, page: int = 1, limit: int = 10):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    skip = (page - 1) * limit
    transactions = list(transaction_collection.find({"user_id": user_id}).skip(skip).limit(limit))
    for transaction in transactions:
        transaction["_id"] = str(transaction["_id"])
    
    total_transactions = transaction_collection.count_documents({"user_id": user_id})

    return {
        "transactions": transactions,
        "total": total_transactions,
        "page": page,
        "limit": limit
    }


async def transaction_detail(transaction_id: str):
    transaction = transaction_collection.find_one({"_id": ObjectId(transaction_id)})
    if not transaction:
        raise ValueError("Transaction not found")
    transaction["_id"] = str(transaction["_id"])
    return transaction
