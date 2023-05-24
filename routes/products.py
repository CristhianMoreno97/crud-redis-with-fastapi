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
    
@routes_product.get("/get/{id}")
def get(id: str):
    try:
        return list(filter(lambda product: product["id"] == id, fake_db))
    except Exception as e:
        return {"error": e}
    
@routes_product.delete("/delete/{id}")
def delete(id: str):
    try:
        product = list(filter(lambda product: product["id"] == id, fake_db))
        if product:
            fake_db.remove(product)
        return {"message": "Product deleted"}
    except Exception as e:
        return {"error": e}