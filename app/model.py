from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float


class CreateProduct(Product):
    id: None


class UpdateProduct(BaseModel):
    name: str | None
    category: str | None
    price: float | None
