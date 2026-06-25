from abc import ABC, abstractmethod

from src.domain.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get(self, order_id: int) -> Order | None:
        pass

    @abstractmethod
    def list(self) -> list[Order]:
        pass
