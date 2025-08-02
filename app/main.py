from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List
from app import database, models

class ProductIn(BaseModel):
    name: str = Field(...)
    sku: str = Field(...)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

class ProductOut(ProductIn):
    id: int
    created_at: str

    class Config:
        orm_mode = True

app = FastAPI()

@app.post("/products", response_model=ProductOut)
async def add_product(product: ProductIn):
    # Write async DB logic to add a product and return ProductOut
    pass

@app.get("/products", response_model=List[ProductOut])
async def list_products():
    # Write async DB logic to fetch all products
    pass
