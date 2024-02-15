from typing import List

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(length=50), nullable=False)
    # blog: Mapped[List['Blog']] = relationship()
