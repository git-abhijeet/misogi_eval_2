from config.db import user_collection, transaction_collection
from bson.objectid import ObjectId
from fastapi import HTTPException
from datetime import datetime


async def user_transaction(user_id: str):
    # user = user_collection.find_one({"user_id": ObjectId(user_id)})
    # if not user:
    #     raise ValueError("User not found")

    transactions = list(transaction_collection.find({"user_id": user_id}))
    for transaction in transactions:
        transaction["_id"] = str(transaction["_id"])
    return transactions


async def transaction_detail(transaction_id: str):
    transaction = transaction_collection.find_one({"_id": ObjectId(transaction_id)})
    if not transaction:
        raise ValueError("Transaction not found")
    transaction["_id"] = str(transaction["_id"])
    return transaction
