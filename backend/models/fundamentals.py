from sqlalchemy import Column, Integer, BigInteger, Double, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.database import Base  # Assuming you have a database connection setup


class Fundamentals(Base):
    __tablename__ = "fundamentals"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)  # Foreign key reference to stocks table
    market_cap = Column(BigInteger)
    ebitda = Column(BigInteger)
    pe_ratio = Column(Double)
    peg_ratio = Column(Double)
    book_value = Column(Double)
    dividend_per_share = Column(Double)
    dividend_yield = Column(Double)
    eps = Column(Double)
    revenue_ttm = Column(BigInteger)
    gross_profit_ttm = Column(BigInteger)
    operating_margin_ttm = Column(Double)
    return_on_assets_ttm = Column(Double)
    return_on_equity_ttm = Column(Double)
    quarterly_earnings_growth_yoy = Column(Double)
    quarterly_revenue_growth_yoy = Column(Double)
    price_to_sales_ratio_ttm = Column(Double)
    price_to_book_ratio = Column(Double)
    ev_to_revenue = Column(Double)
    ev_to_ebitda = Column(Double)
    beta = Column(Double)
    high_52_week = Column(Double)
    low_52_week = Column(Double)
    shares_outstanding = Column(BigInteger)

    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    # Relationship with stocks table
    stocks = relationship("Stocks", back_populates="fundamentals")
