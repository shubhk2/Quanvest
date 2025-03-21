from sqlalchemy import Column, Integer, BigInteger, Date, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base

class IncomeStatement(Base):
    __tablename__ = "income_statement"

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    fiscal_date = Column(Date)

    # Revenue & Profitability
    total_revenue = Column(BigInteger)
    gross_profit = Column(BigInteger)
    operating_income = Column(BigInteger)
    net_income = Column(BigInteger)

    # Costs & Expenses
    cost_of_revenue = Column(BigInteger)
    operating_expenses = Column(BigInteger)
    research_and_development = Column(BigInteger)
    selling_general_admin = Column(BigInteger)

    # Interest & Taxes
    interest_expense = Column(BigInteger)
    income_before_tax = Column(BigInteger)
    income_tax_expense = Column(BigInteger)

    # No need for EBITDA (already in fundamentals)


    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    stocks = relationship("Stocks", back_populates="income_statement")
