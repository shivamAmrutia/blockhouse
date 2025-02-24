from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi import WebSocket
from .. import schemas, crud
from ..database import get_db
from .websocket import active_connections, OrderStatusUpdate

router = APIRouter()

@router.post("/orders", response_model=schemas.Order)
async def create_order(order: schemas.Order, db: Session = Depends(get_db)):
    # Check for duplicate order (optional)
    existing_order = db.query(crud.OrderModel).filter(
        crud.OrderModel.symbol == order.symbol,
        crud.OrderModel.price == order.price,
        crud.OrderModel.quantity == order.quantity,
        crud.OrderModel.order_type == order.order_type
    ).first()

    if existing_order:
        raise HTTPException(status_code=400, detail="Duplicate order detected")

    # Create the order in the database
    db_order = crud.create_order(db=db, order=order)

    # Notify WebSocket clients
    order_status_update = OrderStatusUpdate(
        id=db_order.id,
        symbol=db_order.symbol,
        price=db_order.price,
        quantity=db_order.quantity,
        order_type=db_order.order_type
    )

    for websocket in active_connections:
        await websocket.send_json(order_status_update.dict())

    return db_order

@router.get("/orders", response_model=List[schemas.Order])
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db=db)
