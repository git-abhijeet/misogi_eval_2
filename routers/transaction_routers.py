from fastapi import APIRouter
from handlers.transaction_handler import get_user_transactions_handler, get_transaction_detail_handler

router = APIRouter()


router.get("/transactions/{user_id}")(get_user_transactions_handler)
router.get("/transactions/detail/{transaction_id}")(get_transaction_detail_handler)
