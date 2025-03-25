from sqlalchemy.orm import Session
from backend.models.cash_flow import CashFlow
from backend.schemas import CashFlowCreate


def get_cash_flow_by_stock_id(db: Session, stock_id: int):
    return db.query(CashFlow).filter(CashFlow.stock_id == stock_id).order_by(CashFlow.fiscal_date.desc()).first()


def get_cash_flows(db: Session, stock_id:int,skip: int = 0, limit: int = 10):
    return db.query(CashFlow).filter(CashFlow.stock_id==stock_id).offset(skip).limit(limit).all()


def create_cash_flow(db: Session, cash_flow: CashFlowCreate):
    db_cash_flow = CashFlow(**cash_flow.model_dump())
    db.add(db_cash_flow)
    db.commit()
    db.refresh(db_cash_flow)
    return db_cash_flow


def update_cash_flow_by_stock_id(db: Session, stock_id: int, updated_data: dict):
    cash_flow = db.query(CashFlow).filter(CashFlow.stock_id == stock_id).order_by(CashFlow.fiscal_date.desc())

    if cash_flow.first() is None:
        return None  # No cash flow data exists

    cash_flow.update(updated_data)
    db.commit()
    return cash_flow.first()


def delete_cash_flow_by_stock_id(db: Session, stock_id: int):
    cash_flow = db.query(CashFlow).filter(CashFlow.stock_id == stock_id).order_by(CashFlow.fiscal_date.desc()).first()

    if cash_flow is None:
        return None  # Cash flow data not found

    db.delete(cash_flow)
    db.commit()
    return cash_flow
