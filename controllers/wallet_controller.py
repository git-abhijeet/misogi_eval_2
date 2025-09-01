from fastapi import HTTPException
from config.db import user_collection, transaction_collection
from bson.objectid import ObjectId
from schemas.wallet_schemas import Wallet, WalletTransaction
from datetime import datetime



async def get_balance(user_id: str):
    # Logic to get the user's wallet balance    
    try:
        
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        user_data = {}
        user_data["user_id"] = str(user["_id"])
        user_data["last_updated"] = user.get("updated_at")
        user_data["balance"] = user.get("balance", 0)
        print("🐍 [wallet_controller.py:14] ▶", user_data)
        # user_balance = user..get("balance", 0)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return Wallet(**user_data)


async def add_balance(user_id: str, data: WalletTransaction):

    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")
    

    user["balance"] = user.get("balance", 0) + data.amount
    user["description"] = data.description
    user_data = user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"balance": user["balance"], "updated_at": datetime.utcnow()}})
    print("🐍 [wallet_controller.py:32] ▶", user_data)

    transaction_data = {
        "user_id": user_id,
        "transaction_type": "CREDIT",
        "amount": data.amount,
        "description": data.description,
        "created_at": datetime.utcnow()
    }
    transaction = transaction_collection.insert_one(transaction_data)
    new_transaction_data = {
        "id": str(transaction.inserted_id),
        "user_id": user_id,
        "amount": data.amount,
        "new_balance": user["balance"],
        "transaction_type": "CREDIT"
    }
    print("🐍 [wallet_controller.py:39] ▶", transaction)

    return new_transaction_data


async def withdraw_balance(user_id: str, data: WalletTransaction):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.get("balance", 0) < data.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")

    user["balance"] = user.get("balance", 0) - data.amount
    user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"balance": user["balance"], "updated_at": datetime.utcnow()}})

    transaction_data = {
        "user_id": user_id,
        "transaction_type": "DEBIT",
        "amount": data.amount,
        "description": data.description,
        "created_at": datetime.utcnow()
    }
    transaction = transaction_collection.insert_one(transaction_data)
    new_transaction_data = {
        "id": str(transaction.inserted_id),
        "user_id": user_id,
        "amount": data.amount,
        "new_balance": user["balance"],
        "transaction_type": "DEBIT"
    }
    print("🐍 [wallet_controller.py:39] ▶", transaction)

    return new_transaction_data



