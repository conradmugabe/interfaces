"""Todo SQL Model"""
from uuid import uuid4

from sqlalchemy import Column, UUID, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TodoModel(Base):
    """Todo Model"""

    __tablename__ = "Todo"

    id = Column(UUID, primary_key=True, default=uuid4)

    title = Column(String)
    completed = Column(Boolean)
