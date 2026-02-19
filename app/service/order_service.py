from uuid import UUID
from typing import :ist
from app.domain.order import Order
from app.domain.repository import OrderRepository


class OrdderService:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, amount: float) -> Order:
        order = Order.create(amount)
        self.repository.save(order)
        return order
  
    def list_orders(self) -> List[Order]:
        return self.repository.list()

    def mark_paid(self, order_id: UUID):
        order= self.repository.get(order_id)
        order.mark_paid()
        self.repository.save(order)
