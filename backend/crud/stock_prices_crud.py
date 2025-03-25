from sqlalchemy.orm import Session
from backend.models.stock_prices import StockPrices
from backend.schemas import StockPricesCreate


def get_stock_price_by_stock_id(db: Session, stock_id: int):
    return db.query(StockPrices).filter(StockPrices.stock_id == stock_id).order_by(StockPrices.date.desc()).first()


def get_stock_prices(db: Session, stock_id:int,skip: int = 0, limit: int = 10):
    return db.query(StockPrices).filter(StockPrices.stock_id==stock_id).offset(skip).limit(limit).all()


def create_stock_price(db: Session, stock_price: StockPricesCreate):
    db_stock_price = StockPrices(**stock_price.model_dump())
    db.add(db_stock_price)
    db.commit()
    db.refresh(db_stock_price)
    return db_stock_price


def update_stock_price_by_stock_id(db: Session, stock_id: int, updated_data: dict):
    stock_price = db.query(StockPrices).filter(StockPrices.stock_id == stock_id).order_by(StockPrices.date.desc())

    if stock_price.first() is None:
        return None  # No stock price data exists

    stock_price.update(updated_data)
    db.commit()
    return stock_price.first()


def delete_stock_price_by_stock_id(db: Session, stock_id: int):
    stock_price = db.query(StockPrices).filter(StockPrices.stock_id == stock_id).order_by(
        StockPrices.date.desc()).first()

    if stock_price is None:
        return None  # Stock price not found

    db.delete(stock_price)
    db.commit()
    return stock_price
