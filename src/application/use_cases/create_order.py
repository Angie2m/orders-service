from src.domain.entities.order import Order
from src.domain.repositories.order_repository import OrderRepository


class CreateOrderUseCase:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, customer_name: str, total: float):
        order = Order(id=None, customer_name=customer_name, total=total)

        return self.repository.save(order)
