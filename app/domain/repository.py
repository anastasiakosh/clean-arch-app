fom abc import ABC, abstractmethod
from typinh import List
from uuid import UUID
from .order import Order


class OrderRepository(ABC):

    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstactmethod
    def get(self, order_id: UUID) -> Order:

    @abstactmethod
    def list(self) -> List[Order]:
        pass
