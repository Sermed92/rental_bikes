import pytest
from ..rental.rental_type import RentalType
from ..rental.order import Order
from .. rental.rental import Rental

@pytest.fixture
def rental_type():
    return RentalType.hourly

@pytest.fixture
def order(rental_type):
    return Order(rental_type, 1, 1)

@pytest.fixture
def order_with_discount(rental_type):
    return Order(rental_type, 3, 1)

@pytest.fixture
def big_order(rental_type):
    return Order(rental_type, 8, 1)

def test_with_invalid_order():
    with pytest.raises(TypeError):
        Rental(None, 'Sergio')

def test_rental(order):
    rental = Rental(order, 'Sergio')
    assert rental.FAMILY_DISCOUNT == 0.3
    assert rental.MAX_BIKES_DISCOUNT == 3
    assert rental.client == 'Sergio'
    assert rental.has_family_discount() == False
    assert rental.basic_price() == 5
    assert rental.discount_price() == 3.5
    assert rental.total_price == 5
    assert str(rental) == 'Rental by hours for Sergio, total price = 5'

def test_rental_with_family_discount(order_with_discount):
    rental = Rental(order_with_discount, 'Sergio')
    assert rental.has_family_discount() == True
    assert rental.total_price == 13.5
    assert str(rental) == 'Rental by hours for Sergio, with family discount, total price = 13.5'

def test_rental_with_big_order(big_order):
    rental = Rental(big_order, 'Sergio')
    assert rental.total_price == 35.5
    assert str(rental) == 'Rental by hours for Sergio, with family discount, total price = 35.5'
