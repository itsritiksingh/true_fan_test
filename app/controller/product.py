from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.model import Product, CreateProduct, UpdateProduct
from app.dao import product

router = APIRouter()


@router.get("/{product_id}", response_model=Product)
async def read_product(product_id: int, db=Depends(get_db)):
    db_product = await product.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.get("/", response_model=list[Product])
async def read_products(db=Depends(get_db)):
    products = await product.get_products(db)
    return products


@router.post("/", response_model=Product)
async def create_product(product_body: CreateProduct, db=Depends(get_db)):
    return await product.create_product(db, product_body)


@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, product_body: UpdateProduct, db=Depends(get_db)):
    db_product = await product.update_product(db, product_id, product_body)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/{product_id}", response_model=Product)
async def delete_product(product_id: int, db=Depends(get_db)):
    db_product = await product.delete_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
