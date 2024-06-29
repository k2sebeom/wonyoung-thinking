from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session

from core.db import Base
from datetime import datetime


class Thinking(Base):
    __tablename__ = "thinkings"

    id = Column(Integer, primary_key=True)
    negative = Column(String)
    positive = Column(String)

    created_at = Column(DateTime, default=datetime.now)


def store_thinking(
    db: Session,
    negative: str,
    positive: str,
):
    thinking = Thinking(
        negative=negative,
        positive=positive,
    )
    db.add(thinking)
    db.commit()
    db.refresh(thinking)
    return thinking
