from sqlalchemy.orm import Session
from backend.models.fundamentals import Fundamentals
from backend.schemas import FundamentalsCreate


def get_fundamental_by_stock_id(db: Session, stock_id: int):
    return db.query(Fundamentals).filter(Fundamentals.stock_id == stock_id).first()


def get_fundamentals(db: Session,stock_id: int, skip: int = 0, limit: int = 10):
    return db.query(Fundamentals).filter(Fundamentals.stock_id==stock_id).offset(skip).limit(limit).all()


def create_fundamental(db: Session, fundamental: FundamentalsCreate):
    db_fundamental = Fundamentals(**fundamental.model_dump())
    db.add(db_fundamental)
    db.commit()
    db.refresh(db_fundamental)
    return db_fundamental


def update_fundamental_by_stock_id(db: Session, stock_id: int, updated_data: dict):
    fundamental = db.query(Fundamentals).filter(Fundamentals.stock_id == stock_id)

    if fundamental.first() is None:
        return None  # Fundamental data doesn't exist

    fundamental.update(updated_data)
    db.commit()
    return fundamental.first()


def delete_fundamental_by_stock_id(db: Session, stock_id: int):
    fundamental = db.query(Fundamentals).filter(Fundamentals.stock_id == stock_id).first()

    if fundamental is None:
        return None  # Fundamental not found

    db.delete(fundamental)
    db.commit()
    return fundamental
