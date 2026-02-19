from app.domain.order import Order


def test_create_order():
    order = Order.create(100)
    assert order.amount == 100


def test_individual_amount():
    import pytest
    with pytest.raises(ValueError):
        Order.create(-1)
