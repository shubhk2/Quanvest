from sqlalchemy import Column,BigInteger, Date,Integer, String, Float, ForeignKey, TIMESTAMP, func, DateTime

from backend.database import Base
from sqlalchemy.orm import relationship

class CashFlow(Base):
    __tablename__ = "cash_flow"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    fiscal_date = Column(Date)

    # Cash Flow Categories
    operating_cash_flow = Column(BigInteger)
    cashflow_from_investment = Column(BigInteger)
    cashflow_from_financing = Column(BigInteger)

    # Asset & Liability Changes
    change_in_operating_assets = Column(BigInteger)
    change_in_operating_liabilities = Column(BigInteger)
    change_in_receivables = Column(BigInteger)
    change_in_inventory = Column(BigInteger)

    # Expenses & Repurchases
    capital_expenditure = Column(BigInteger)
    payments_for_repurchase_of_common_stock = Column(BigInteger)
    dividend_payout = Column(BigInteger)

    # Timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    stocks = relationship("Stocks", back_populates="cash_flow")
