from sqlalchemy.orm import Session

from src.domain.entities.order import Order
from src.infrastructure.database.models import OrderModel


class SQLAlchemyOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, order: Order):
        model = OrderModel(customer_name=order.customer_name, total=order.total)

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return Order(
            id=int(model.id),
            customer_name=str(model.customer_name),
            total=float(model.total),
        )

    def get(self, order_id: int):
        model = self.db.query(OrderModel).filter(OrderModel.id == order_id).first()

        if not model:
            return None

        return Order(
            id=int(model.id),
            customer_name=str(model.customer_name),
            total=float(model.total),
        )

    def list(self):
        models = self.db.query(OrderModel).all()

        return [
            Order(id=m.id, customer_name=m.customer_name, total=m.total) for m in models
        ]
