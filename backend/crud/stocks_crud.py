from sqlalchemy.orm import Session
from backend.models.stocks import Stocks
from backend.schemas import StocksCreate, StocksUpdate

def get_stock_by_symbol(db: Session, stock_symbol: str):
    return db.query(Stocks).filter(Stocks.symbol == stock_symbol).first()

def get_stock_id_by_symbol(db: Session, stock_symbol: str):
    stock = db.query(Stocks).filter(Stocks.symbol == stock_symbol).first()
    return stock.id if stock else None

def get_stocks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Stocks).offset(skip).limit(limit).all()

def create_stock(db: Session, stock: StocksCreate):
    db_stock = Stocks(**stock.model_dump())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock


def update_stock_by_symbol(db: Session, stock_symbol: str, updated_data: dict):
    stock = db.query(Stocks).filter(Stocks.symbol == stock_symbol)

    if stock.first() is None:
        return None  # Stock doesn't exist

    stock.update(updated_data)
    db.commit()
    return stock.first()


def delete_stock_by_symbol(db: Session, stock_symbol: str):
    stock = db.query(Stocks).filter(Stocks.symbol == stock_symbol).first()

    if stock is None:
        return None  # Stock not found

    db.delete(stock)
    db.commit()
    return stock