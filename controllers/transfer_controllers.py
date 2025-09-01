from fastapi import HTTPException
from config.db import user_collection, transaction_collection
from schemas.transfer_schemas import TransferRequest
from bson.objectid import ObjectId
from datetime import datetime




async def transfer_money(transfer_request: TransferRequest):
    print("🐍 [transfer_controllers.py:11] ▶", transfer_request)
    # try:
    print("🐍 [transfer_controllers.py:6] ▶", transfer_request)

    # Check if sender has sufficient balance
    sender = user_collection.find_one({"_id": ObjectId(transfer_request.sender_user_id)})
    if not sender:
        raise HTTPException(status_code=404, detail="Sender not found")
    print("🐍 [transfer_controllers.py:16] ▶", sender)
    
    if transfer_request.amount <= 0:
        raise HTTPException(status_code=400, detail="Transfer amount must be greater than zero")

    if sender["balance"] < transfer_request.amount:
        data = {
            "error": "Insufficient balance",
            "current_balance": sender["balance"],
            "required_amount": transfer_request.amount
        }
        raise HTTPException(status_code=400, detail=data)

    # Add amount to recipient
    recipient = user_collection.find_one({"_id": ObjectId(transfer_request.recipient_user_id)})
    if not recipient:
        raise HTTPException(status_code=404, detail="Recipient not found")
    print("🐍 [transfer_controllers.py:25] ▶", recipient)
    
    # Deduct amount from sender
    user_collection.update_one({"_id": ObjectId(transfer_request.sender_user_id)}, {"$inc": {"balance": -transfer_request.amount}})


    user_collection.update_one({"_id": ObjectId(transfer_request.recipient_user_id)}, {"$inc": {"balance": +transfer_request.amount}})

    # Create transaction record
    transaction = {
        "user_id": transfer_request.sender_user_id,
        "transaction_type": "TRANSFER_OUT",
        "amount": transfer_request.amount,
        "description": transfer_request.description,
        "recipient_user_id": transfer_request.recipient_user_id,
        "created_at": datetime.utcnow()
    }
    transaction_data = transaction_collection.insert_one(transaction)
    print("🐍 [transfer_controllers.py:45] ▶", transaction_data)


    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    
    return {
        "transfer_id": str(transaction_data.inserted_id),
        "amount": transfer_request.amount,
        "sender_new_balance": sender["balance"] - transfer_request.amount,
        "recipient_new_balance": recipient["balance"] + transfer_request.amount,
        "status": "completed"
    }

