from fastapi import FastAPI
from routers.user_routers import router as user_router
from routers.wallet_routers import router as wallet_router
from routers.transfer_routers import router as transfer_router
from routers.transaction_routers import router as transaction_router
from config.db import client



app = FastAPI()

app.include_router(user_router, tags=["user"])
app.include_router(wallet_router, tags=["wallet"])
app.include_router(transfer_router, tags=["transfer"])
app.include_router(transaction_router, tags=["transaction"])


@app.on_event("startup")
async def startup_db_client():
    client.admin.command('ping')
    print("Connected to the MongoDB database!")

@app.get("/")
def read_root():
    return {"Hello": "World"}

