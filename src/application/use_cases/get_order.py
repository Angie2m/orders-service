from src.domain.repositories.order_repository import OrderRepository


class GetOrderUseCase:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_id: int):
        return self.repository.get(order_id)
