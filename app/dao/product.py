from typing import List
from asyncpg import Pool, Record
from app.model import CreateProduct, UpdateProduct


def record_to_dict(row: Record):
    if not row:
        return None
    return dict(row.items())


def list_record_to_dict(rows: List[Record]):
    ret = []
    for row in rows:
        ret.append(record_to_dict(row))

    return ret


async def get_product(pool: Pool, product_id: int):
    async with pool.acquire() as connection:
        product = await connection.fetchrow("SELECT * FROM products WHERE id = $1", product_id)
    return record_to_dict(product)


async def get_products(pool: Pool):
    async with pool.acquire() as connection:
        products = await connection.fetch("SELECT * FROM products")
    return list_record_to_dict(products)


async def create_product(pool: Pool, product: CreateProduct):
    async with pool.acquire() as connection:
        result = await connection.fetchrow(
            "INSERT INTO products (name, category, price) VALUES ($1, $2, $3) RETURNING *",
            product.name,
            product.category,
            product.price,
        )
    return record_to_dict(result)


async def update_product(pool: Pool, product_id: int, product: UpdateProduct):
    async with pool.acquire() as connection:
        result = await connection.fetchrow(
            "UPDATE products SET name = $1, category = $2, price = $3 WHERE id = $4 RETURNING *",
            product.name,
            product.category,
            product.price,
            product_id,
        )
    return record_to_dict(result)


async def delete_product(pool: Pool, product_id: int):
    async with pool.acquire() as connection:
        result = await connection.fetchrow("DELETE FROM products WHERE id = $1 RETURNING *", product_id)
    return record_to_dict(result)
