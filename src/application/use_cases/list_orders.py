from src.domain.repositories.order_repository import OrderRepository


class ListOrdersUseCase:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self):
        return self.repository.list()
