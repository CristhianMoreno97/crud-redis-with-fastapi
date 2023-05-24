from fastapi import APIRouter
from schemas.product import Product
from redis_client.crud import delete_hash, get_hash, save_hash

routes_product = APIRouter()

fake_db = []

@routes_product.post("/create", response_model=Product)
def create(product: Product):
    try:
        # save on database
        fake_db.append(product.dict())
        # save on redis
        save_hash(key=product.dict()["id"], data=product.dict())
        return product
    except Exception as e:
        return {"error": e}
    
@routes_product.get("/get/{id}")
def get(id: str):
    try:
        # try get from redis
        product = get_hash(key=id)
        if len(product) > 0:
            return product

        # try get from database
        product = list(filter(lambda product: product["id"] == id, fake_db))[0]
        
        # save on redis
        save_hash(key=id, data=product)

        return product
    except Exception as e:
        return {"error": e}
    
@routes_product.delete("/delete/{id}")
def delete(id: str):
    try:
        # delete from redis
        keys = Product.__fields__.keys()
        delete_hash(key=id, keys=keys)
        # delete from database
        product = list(filter(lambda product: product["id"] == id, fake_db))[0]
        if product:
            fake_db.remove(product)
        return {"message": "Product deleted"}
    except Exception as e:
        return {"error": e}
