from sqlalchemy import Column, Integer, String
from app.db import Base


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

