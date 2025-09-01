from fastapi import HTTPException
from controllers.user_controllers import create_user, get_user, update_user
from schemas.user_schemas import User, CreateUser, UpdateUser

async def create_user_handler(user: CreateUser):
    try:
        print("🐍 [user_handler.py:6] ▶", user)
        user_data = await create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_data

async def get_user_handler(user_id: str):
    try:
        print("🐍 [user_handler.py:12] ▶", user_id)
        user_data = await get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_data

async def update_user_handler(user_id: str, user: UpdateUser):
    try:
        print("🐍 [user_handler.py:18] ▶", user_id, user)
        user_data = await update_user(user_id, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_data
