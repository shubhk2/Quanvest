from sqlalchemy.orm import Session
from backend.models.balance_sheet import BalanceSheet
from backend.schemas import BalanceSheetCreate

def get_balance_sheet(db: Session, balance_sheet_id: int):
    return db.query(BalanceSheet).filter(BalanceSheet.id == balance_sheet_id).first()


def get_balance_sheets(db: Session, stock_id: int, skip: int = 0, limit: int = 10):
    return db.query(BalanceSheet).filter(BalanceSheet.stock_id == stock_id).offset(skip).limit(limit).all()

def create_balance_sheet(db: Session, balance_sheet: BalanceSheetCreate):
    db_balance_sheet = BalanceSheet(**balance_sheet.model_dump())
    db.add(db_balance_sheet)
    db.commit()
    db.refresh(db_balance_sheet)
    return db_balance_sheet

def update_balance_sheet(db: Session, balance_sheet_id: int, updated_data: dict):
    balance_sheet = db.query(BalanceSheet).filter(BalanceSheet.id == balance_sheet_id)

    if balance_sheet.first() is None:
        return None  # Balance sheet doesn't exist

    balance_sheet.update(updated_data)
    db.commit()
    return balance_sheet.first()

def delete_balance_sheet(db: Session, balance_sheet_id: int):
    balance_sheet = db.query(BalanceSheet).filter(BalanceSheet.id == balance_sheet_id).first()

    if balance_sheet is None:
        return None  # Balance sheet not found

    db.delete(balance_sheet)
    db.commit()
    return balance_sheet