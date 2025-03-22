# backend/script_runner.py
from backend.database import Base
from backend.models.stocks import Stocks
from backend.models.stock_prices import StockPrices
from backend.models.fundamentals import Fundamentals
from backend.models.balance_sheet import BalanceSheet
from backend.models.cash_flow import CashFlow
from backend.models.income_statement import IncomeStatement

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:shubhk2004@localhost/quanvest"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    init_db()
