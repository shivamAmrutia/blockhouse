from sqlalchemy.orm import Session
from app.models import OrderModel
from app.schemas import Order

def create_order(db: Session, order: Order):
    db_order = OrderModel(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session):
    return db.query(OrderModel).all()
