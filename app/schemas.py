from pydantic import BaseModel

class Order(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str  # e.g., "buy" or "sell"

    class Config:
        orm_mode = True
