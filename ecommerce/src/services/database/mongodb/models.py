from pydantic import BaseModel, Field
from typing import List
from enum import Enum

#orders
class Status(Enum):
    #request to payments:
    # if payment processed then delivery in process else cancelled
    DELIVERY_INPROCESS = "delivery in process"
    CANCELLED = "cancelled"
    DELIVERED = "delivered"

class OrderDetails(BaseModel):
    product_id : int
    quantity : int
    total : float

class Orders(BaseModel):
    user_id : int
    order_details : List[OrderDetails]
    total_amount : float
    # await for the payment details
    payment_id : str = Field(default=None)
    payment_status : str = Field(default=None)
    order_status : Status = Field(default=None)


#products
class Description(BaseModel):
    title : str
    content : str

class Product(BaseModel):
    product_name : str
    category_id : str = Field(default=None)
    product_description : List[Description]
    mrp : float
    stock : int

class Category(BaseModel):
    category_name : str
    category_description : List[Description]
