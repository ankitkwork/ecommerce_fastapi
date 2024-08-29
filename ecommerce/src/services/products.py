from fastapi import APIRouter
from .database.mongodb.models import Category,Product
from .database.mongodb.database import category_collection, product_collection

product_router=APIRouter(prefix='/products', tags=['products'])

@product_router.post("/new_category")
def add_new_category(category : Category):
    category_data={
        "category_name" : category.category_name,
        "category_description" : [{
            "title" : details.title,
            "content" : details.content
        }
        for details in category.category_description]
    }
    category_collection.insert_one(category_data)


@product_router.post("/new_product/")
def add_new_product(product : Product, category_id):
    product_data={
        "product_name" : product.product_name,
        "category_id" : category_id,
        "product_description" : [{
            "title" : details.title,
            "content" : details.content
        }
        for details in product.product_description],
        "mrp" : product.mrp,
        "stock" : product.stock
    }
    product_collection.insert_one(product_data)