from sqlalchemy.orm import Session
from backend.models.income_statement import IncomeStatement
from backend.schemas import IncomeStatementCreate


def get_income_statement_by_stock_id(db: Session, stock_id: int):
    return db.query(IncomeStatement).filter(IncomeStatement.stock_id == stock_id).order_by(
        IncomeStatement.fiscal_date.desc()).first()


def get_income_statements(db: Session, stock_id,skip: int = 0, limit: int = 10):
    return db.query(IncomeStatement).filter(IncomeStatement.stock_id==stock_id).offset(skip).limit(limit).all()


def create_income_statement(db: Session, income_statement: IncomeStatementCreate):
    db_income_statement = IncomeStatement(**income_statement.model_dump())
    db.add(db_income_statement)
    db.commit()
    db.refresh(db_income_statement)
    return db_income_statement


def update_income_statement_by_stock_id(db: Session, stock_id: int, updated_data: dict):
    income_statement = db.query(IncomeStatement).filter(IncomeStatement.stock_id == stock_id).order_by(
        IncomeStatement.fiscal_date.desc())

    if income_statement.first() is None:
        return None  # No income statement data exists

    income_statement.update(updated_data)
    db.commit()
    return income_statement.first()


def delete_income_statement_by_stock_id(db: Session, stock_id: int):
    income_statement = db.query(IncomeStatement).filter(IncomeStatement.stock_id == stock_id).order_by(
        IncomeStatement.fiscal_date.desc()).first()

    if income_statement is None:
        return None  # Income statement data not found

    db.delete(income_statement)
    db.commit()
    return income_statement
