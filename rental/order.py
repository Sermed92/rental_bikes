from .rental_type import RentalType


class Order(object):
    
    def __init__(self, rental_type, bikes, duration):

        if (not (rental_type in RentalType)):
            raise TypeError('Argument rental_type must be a valid RentalType')
        else:
            self.rental_type = rental_type

        if (bikes < 1):
            raise ValueError('Rented bikes must be a positive value')
        else:
            self.bikes = bikes

        if (duration < 1):
            raise ValueError('Duration must be a positive value')
        else:
            self.duration = duration
    
    def __str__(self):
        return str(self.rental_type)
