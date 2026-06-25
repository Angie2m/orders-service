from sqlalchemy import Column, Float, Integer, String

from src.infrastructure.database.db import Base


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    total = Column(Float)
