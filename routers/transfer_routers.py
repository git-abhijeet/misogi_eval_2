from fastapi import APIRouter
from handlers.transfer_handler import transfer_money_handler

router = APIRouter()


router.post("/transfer/")(transfer_money_handler)
