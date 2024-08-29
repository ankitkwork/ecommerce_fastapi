from fastapi import FastAPI
from src.authentication import auth_router
from src.services.orders import order_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(order_router)