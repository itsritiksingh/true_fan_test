import asyncpg
from .settings import settings

_pool = None


async def get_db():
    global _pool
    if _pool is None:
        _pool = await asyncpg.create_pool(
            dsn=settings.POSTGRES_URL.unicode_string(), max_inactive_connection_lifetime=3
        )
    return _pool
