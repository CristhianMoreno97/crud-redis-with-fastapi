from fastapi import APIRouter
from schemas.product import Product

routes_product = APIRouter()

fake_db = []

@routes_product.post("/create", response_model=Product)
def create(product: Product):
    try:
        fake_db.append(product.dict())
        return product
    except Exception as e:
        return {"error": e}