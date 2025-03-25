from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.crud import stocks_crud, stock_prices_crud, cash_flow_crud, income_statements_crud, fundamentals_crud,balance_sheet_crud
from backend.models.stocks import Stocks
from backend.schemas import StocksCreate, StocksUpdate, StockPricesCreate, CashFlowCreate, IncomeStatementCreate, FundamentalsCreate, BalanceSheetCreate

router = APIRouter()

###  STOCKS CRUD ###
@router.get("/stocks/{symbol}")
def get_stock(symbol: str, db: Session = Depends(get_db)):
    stock = stocks_crud.get_stock_by_symbol(db, symbol)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.post("/stocks/")
def create_stock(stock: StocksCreate, db: Session = Depends(get_db)):
    return stocks_crud.create_stock(db, stock)

@router.put("/stocks/{symbol}")
def update_stock(symbol: str, stock_update: StocksUpdate, db: Session = Depends(get_db)):
    updated_stock = stocks_crud.update_stock_by_symbol(db, symbol, stock_update.dict())
    if not updated_stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return updated_stock

@router.delete("/stocks/{symbol}")
def delete_stock(symbol: str, db: Session = Depends(get_db)):
    deleted_stock = stocks_crud.delete_stock_by_symbol(db, symbol)
    if not deleted_stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return {"detail": "Stock deleted successfully"}

###  STOCK PRICES CRUD ###
@router.get("/stock_prices/{symbol}")
def get_stock_price(symbol: str, db: Session = Depends(get_db)):
    stock_id = stocks_crud.get_stock_id_by_symbol(db, symbol)
    if not stock_id:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock_prices_crud.get_stock_price_by_stock_id(db, stock_id)

@router.post("/stock_prices/")
def create_stock_price(stock_price: StockPricesCreate, db: Session = Depends(get_db)):
    return stock_prices_crud.create_stock_price(db, stock_price)

@router.put("/stock_prices/{symbol}")
def update_stock_price(symbol: str, stock_price_update: StockPricesCreate, db: Session = Depends(get_db)):
    stock_id = stocks_crud.get_stock_id_by_symbol(db, symbol)
    if not stock_id:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock_prices_crud.update_stock_price_by_stock_id(db, stock_id, stock_price_update.dict())

### CASH FLOW CRUD ###
@router.get("/cash_flows/{symbol}")
def get_cash_flow(symbol: str, db: Session = Depends(get_db)):
    stock_id = stocks_crud.get_stock_id_by_symbol(db, symbol)
    if not stock_id:
        raise HTTPException(status_code=404, detail="Stock not found")
    return cash_flow_crud.get_cash_flow_by_stock_id(db, stock_id)

@router.post("/cash_flows/")
def create_cash_flow(cash_flow: CashFlowCreate, db: Session = Depends(get_db)):
    return cash_flow_crud.create_cash_flow(db, cash_flow)

### 🟢 INCOME STATEMENTS CRUD
@router.get("/income_statements/{symbol}")
def get_income_statement(symbol: str, db: Session = Depends(get_db)):
    stock_id = stocks_crud.get_stock_id_by_symbol(db, symbol)
    if not stock_id:
        raise HTTPException(status_code=404, detail="Stock not found")
    return income_statements_crud.get_income_statement_by_stock_id(db, stock_id)

@router.post("/income_statements/")
def create_income_statement(income_statement: IncomeStatementCreate, db: Session = Depends(get_db)):
    return income_statements_crud.create_income_statement(db, income_statement)

### 🟢 FUNDAMENTALS CRUD
@router.get("/fundamentals/{symbol}")
def get_fundamentals(symbol: str, db: Session = Depends(get_db)):
    stock_id = stocks_crud.get_stock_id_by_symbol(db, symbol)
    if not stock_id:
        raise HTTPException(status_code=404, detail="Stock not found")
    return fundamentals_crud.get_fundamental_by_stock_id(db, stock_id)

@router.post("/fundamentals/")
def create_fundamental(fundamental: FundamentalsCreate, db: Session = Depends(get_db)):
    return fundamentals_crud.create_fundamental(db, fundamental)


### Balance Sheet CRUD
@router.get("/balance_sheets/{symbol}")
def get_balance_sheets(symbol: str, db: Session = Depends(get_db)):
    stock_id = stocks_crud.get_stock_id_by_symbol(db, symbol)
    if not stock_id:
        raise HTTPException(status_code=404, detail="Stock not found")
    return balance_sheet_crud.get_balance_sheets(db, stock_id)

@router.post("/balance_sheets/")
def create_balance_sheet(balance_sheet: BalanceSheetCreate, db: Session = Depends(get_db)):
    return balance_sheet_crud.create_balance_sheet(db, balance_sheet)