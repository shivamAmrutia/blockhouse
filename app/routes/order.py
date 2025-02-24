from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi import WebSocket
from app import schemas, crud
from ..database import get_db
from .websocket import active_connections, OrderStatusUpdate

router = APIRouter()

@router.post("/orders", response_model=schemas.Order)
async def create_order(order: schemas.Order, db: Session = Depends(get_db)):
    # Create the order in the database
    db_order = crud.create_order(db=db, order=order)

    # Create the order status update message
    order_status_update = OrderStatusUpdate(
        id=db_order.id,
        symbol=db_order.symbol,
        price=db_order.price,
        quantity=db_order.quantity,
        order_type=db_order.order_type
    )

    # Broadcast the order status update to all connected WebSocket clients
    for websocket in active_connections:
        await websocket.send_json(order_status_update.dict())

    return db_order

@router.get("/orders", response_model=List[schemas.Order])
def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_orders(db=db, skip=skip, limit=limit)
