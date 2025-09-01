from fastapi import APIRouter
from handlers.user_handler import create_user_handler, get_user_handler, update_user_handler

router = APIRouter()


router.post("/users/")(create_user_handler)
router.get("/users/{user_id}")(get_user_handler)
router.put("/users/{user_id}")(update_user_handler)
