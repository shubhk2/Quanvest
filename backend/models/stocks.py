from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP, func, DateTime
from backend.database import Base
from sqlalchemy.orm import relationship


class Stocks(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    name = Column(String)
    exchange=Column(String)  # Example column for stocks price
    sector=Column(String)
    industry=Column(String)
    currency=Column(String)
    country=Column(String)
    created_at = Column(DateTime, server_default=func.now())  # Default: Current Timestamp
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    fundamentals = relationship("Fundamentals", back_populates="stocks")
    stock_prices = relationship("StockPrices", back_populates="stocks")
    balance_sheet = relationship("BalanceSheet", back_populates="stocks")
    cash_flow = relationship("CashFlow", back_populates="stocks")
    income_statement = relationship("IncomeStatement", back_populates="stocks")