from fastapi import APIRouter, Depends
from app.service.order_service import OrderService
from app.infra.sqlalchemy_repository import SqlAlchemyOrderRepository

router = APIRouter()


def get_service():
    repo = sqlAlchemyOrderRepository()
    return OrderService(repo)

@router.post("/orders")
def create_order(amount: float, service: OrderService = Depends(get_service)):
    return service.create_order(amount)

@router.get("/orders")
def list_orders(service: OrderService = Depends(get_service)):
    return service.list_orders()

