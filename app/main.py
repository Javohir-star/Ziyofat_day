from fastapi import FastAPI

from app.router import (
    dining_table_router,
    order_router
)


app = FastAPI(
    title="Ziyofat Day",
    description="Ziyofat Day - restoran uchun stolni bron qilish va boshqarish tizimi",
)


app.include_router(dining_table_router)
app.include_router(order_router)
