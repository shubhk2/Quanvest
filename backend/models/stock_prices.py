from sqlalchemy import Column, Date,BigInteger,Integer, String, Float, ForeignKey, TIMESTAMP, func, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class StockPrices(Base):
    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)

    month = Column(Date)  # YYYY-MM format to track monthly data
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    adjusted_close_price = Column(Float)
    volume = Column(BigInteger)
    dividend_amount = Column(Float, nullable=True)  # New column for dividends

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    stocks = relationship("Stocks", back_populates="stock_prices")

