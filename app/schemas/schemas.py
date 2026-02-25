from pydantic import BaseModel
from datetime import datetime

class TableBase(BaseModel):
    table_no: str
    capacity: int
    status: str

class TableCreate(TableBase):
    pass

class TableRead(TableBase):
    id: int
    class Config:
        orm_mode = True


class OrderRead(BaseModel):
    id: int
    table_id: int
    waiter_id: int
    status: str

    opened_at: datetime
    submitted_at: datetime | None = None
    closed_at: datetime | None = None
    notes: str | None = None

    class Config:
        orm_mode = True