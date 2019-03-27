import pytest
from ..rental.rental_type import RentalType
from ..rental.order import Order

def test_valid_order():
    order = Order(RentalType.hourly, 1, 1)
    assert order.rental_type.price == 5
    assert str(order) == 'Rental by hours'
    assert order.bikes == 1
    assert order.duration == 1

def test_order_with_invalid_rental_type():
    with pytest.raises(TypeError):
        Order(None, 1, 1)

def test_order_with_invalid_bikes():
    with pytest.raises(ValueError):
        Order(RentalType.daily, 0, 1)

def test_order_with_invalid_duration():
    with pytest.raises(ValueError):
        Order(RentalType.weekly, 1, 0)
