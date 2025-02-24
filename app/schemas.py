from pydantic import BaseModel, Field, constr
from typing import Literal

class Order(BaseModel):
    symbol: constr(strip_whitespace=True, to_upper=True, min_length=1, max_length=5)  # Stock symbol in uppercase
    price: float = Field(..., gt=0, description="Price must be greater than 0")  # Price must be positive
    quantity: int = Field(..., gt=0, description="Quantity must be a positive integer")  # Quantity must be positive
    order_type: Literal["buy", "sell"]  # Order type must be either "buy" or "sell"

    class Config:
        orm_mode = True
