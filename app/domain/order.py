from dataclasses import dataclass
from enum import Enum
from uuid import UUID, uuid4


class OrderStatus(str, Enum):
    CREATED = "created"
    PAID = "paid"
    SHIPPED = "shipped"


@dataclass
class Order:
    id: UUID
    amount: float
    status: OrderStatus = OrderStatus.CREATED

    @staticmethod
    def create(amount: float) -> "Order":
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return Order(id=uuid4(), amount=amount)

    def mark_paid(self):
        if self.status != OrderStatus.CREATED:
            raise ValueError("Order cannot be paid")
        self.status = OrderStatus.PAID
  
