from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from core.gpt import create_thinking
from core.models import store_thinking
from core.db import SessionLocal


think_router = APIRouter(prefix='/thinking')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ThinkReq(BaseModel):
    negative: str

class ThinkResp(BaseModel):
    thinking: str

@think_router.post("/")
async def think(req: ThinkReq, db: Session = Depends(get_db)) -> ThinkResp:
    positive = create_thinking(req.negative)
    store_thinking(db, req.negative, positive)
    return ThinkResp(thinking=positive)
