from sqlalchemy import Column, Integer, BigInteger, Date, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.database import Base  # Assuming you have a database connection setup

class BalanceSheet(Base):
    __tablename__ = "balance_sheet"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    fiscal_date = Column(Date)
    total_assets = Column(BigInteger)
    total_liabilities = Column(BigInteger)
    total_equity = Column(BigInteger)  # total_shareholder_equity
    long_term_debt = Column(BigInteger)
    short_term_debt = Column(BigInteger)
    retained_earnings = Column(BigInteger)
    total_current_assets = Column(BigInteger)
    total_current_liabilities = Column(BigInteger)
    cash_and_cash_equivalents = Column(BigInteger)
    inventory = Column(BigInteger)
    property_plant_equipment = Column(BigInteger)
    goodwill = Column(BigInteger)
    other_current_assets = Column(BigInteger)
    other_non_current_assets = Column(BigInteger)
    deferred_revenue = Column(BigInteger)
    capital_lease_obligations = Column(BigInteger)
    common_stock_shares_outstanding = Column(BigInteger)

    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    stocks = relationship("Stocks", back_populates="balance_sheet")
