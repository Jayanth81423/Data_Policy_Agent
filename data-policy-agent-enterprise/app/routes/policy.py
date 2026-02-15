from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.policy import Policy
from app.schemas.policy_schema import PolicyCreate

router = APIRouter(prefix="/policies", tags=["Policies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_policy(policy: PolicyCreate, db: Session = Depends(get_db)):
    db_policy = Policy(name=policy.name, content=policy.content)
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy
