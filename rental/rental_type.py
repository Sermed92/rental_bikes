from enum import Enum


class RentalType(Enum):

    hourly = (5, 'Rental by hours')
    daily = (20, 'Rental by days')
    weekly = (60, 'Rental by weeks')

    def __init__(self, price, description):
        self.price = price
        self.description = description

    def __str__(self):
        return self.description
