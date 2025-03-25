from pydantic import BaseModel
from typing import Optional
from datetime import date

### 🟢 STOCK SCHEMAS
class StocksBase(BaseModel):
    symbol: str
    name: Optional[str] = None
    industry: Optional[str] = None
    sector: Optional[str] = None

class StocksCreate(StocksBase):  # Used for POST
    pass

class StocksUpdate(StocksBase):  # Used for PUT
    pass

class StocksResponse(StocksBase):  # Used for GET
    id: int
    class Config:
        from_attributes = True

### 🟢 STOCK PRICES SCHEMAS
class StockPricesBase(BaseModel):
    stock_id: int
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int

class StockPricesCreate(StockPricesBase):
    pass

class StockPricesResponse(StockPricesBase):
    id: int
    class Config:
        from_attributes = True

### 🟢 BALANCE SHEET SCHEMAS
class BalanceSheetBase(BaseModel):
    stock_id: int
    year: int
    total_assets: float
    total_liabilities: float
    equity: float

class BalanceSheetCreate(BalanceSheetBase):
    pass

class BalanceSheetResponse(BalanceSheetBase):
    id: int
    class Config:
        from_attributes = True

### 🟢 CASH FLOW SCHEMAS
class CashFlowBase(BaseModel):
    stock_id: int
    year: int
    operating_cash_flow: float
    investing_cash_flow: float
    financing_cash_flow: float

class CashFlowCreate(CashFlowBase):
    pass

class CashFlowResponse(CashFlowBase):
    id: int
    class Config:
        from_attributes = True

### 🟢 INCOME STATEMENT SCHEMAS
class IncomeStatementBase(BaseModel):
    stock_id: int
    year: int
    revenue: float
    net_income: float
    ebitda: float

class IncomeStatementCreate(IncomeStatementBase):
    pass

class IncomeStatementResponse(IncomeStatementBase):
    id: int
    class Config:
        from_attributes = True

### 🟢 FUNDAMENTALS SCHEMAS
class FundamentalsBase(BaseModel):
    stock_id: int
    pe_ratio: Optional[float] = None
    pb_ratio: Optional[float] = None
    roe: Optional[float] = None
    dividend_yield: Optional[float] = None

class FundamentalsCreate(FundamentalsBase):
    pass

class FundamentalsResponse(FundamentalsBase):
    id: int
    class Config:
        from_attributes = True
