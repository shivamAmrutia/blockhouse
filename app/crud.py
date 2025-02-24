from sqlalchemy.orm import Session
from . import models, schemas

def create_order(db: Session, order: schemas.Order):
    db_order = models.OrderModel(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderModel).offset(skip).limit(limit).all()
