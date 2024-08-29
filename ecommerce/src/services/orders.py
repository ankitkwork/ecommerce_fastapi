from fastapi import APIRouter

from .database.mongodb.models import Orders
from .database.mongodb.database import orders_collection
from .database.mongodb.schema import fetchall

from bson import ObjectId
import json

order_router=APIRouter(prefix='/order', tags=['order'])


@order_router.get("/")
async def get_orders():
    return fetchall(orders_collection.find())

@order_router.post("/place_order")
async def order_place(order: Orders):
    order_dict={
        "order_id" : order.order_id,
        "user_id" : order.user_id,
        "order_details" : [{"product_id" : detail.product_id,
                            "quantity" : detail.quantity, 
                            "total" : detail.total}
                            for detail in order.order_details],
        "total_amount" : order.total_amount
    }
    orders_collection.insert_one(order_dict)