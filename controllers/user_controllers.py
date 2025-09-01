from fastapi import HTTPException
from config.db import user_collection
from schemas.user_schemas import CreateUser, UpdateUser
from bson.objectid import ObjectId

async def create_user(user: CreateUser):
    try:
        print("🐍 [user_controllers.py:6] ▶", user)
        old_user = user_collection.find_one({"email": user.email})
        if old_user:
            raise HTTPException(status_code=400, detail="User already exists")
        
        new_user = user.dict()
        create_user = user_collection.insert_one(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return ({"message": "User created successfully", "id": str(create_user.inserted_id)})

async def get_user(user_id: str):
    try:
        print("🐍 [user_controllers.py:17] ▶", user_id)
        user_data = user_collection.find_one({"_id": ObjectId(user_id)})
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")
        user_data["_id"] = str(user_data["_id"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return user_data

async def update_user(user_id: str, user: UpdateUser):
    try:
        print("🐍 [user_controllers.py:31] ▶", user_id, user)
        user_data = user_collection.find_one({"_id": ObjectId(user_id)})
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")
        
        updated_user = user_collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": user.dict()},
            return_document=True
        )
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        updated_user["_id"] = str(updated_user["_id"])
        print("🐍 [user_controllers.py:39] ▶", updated_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return updated_user