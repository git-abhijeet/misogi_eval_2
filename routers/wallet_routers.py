from fastapi import APIRouter
from handlers.wallet_handler import get_balance_handler, add_balance_handler, withdraw_balance_handler

router = APIRouter()


router.get("/wallet/{user_id}/balance")(get_balance_handler)
router.post("/wallet/{user_id}/add-money")(add_balance_handler)
router.post("/wallet/{user_id}/withdraw")(withdraw_balance_handler)

