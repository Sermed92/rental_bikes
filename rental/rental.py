from .order import Order


class Rental(object):
    FAMILY_DISCOUNT = 0.3
    MAX_BIKES_DISCOUNT = 3

    def __init__(self, order, client):
        if (not isinstance(order, Order)):
            raise TypeError('Argument order must be a valid Order')

        self.rental_type =  order.rental_type
        self.bikes = order.bikes
        self.duration = order.duration
        self.client = client
    
    def has_family_discount(self):
        return (self.bikes >= self.MAX_BIKES_DISCOUNT)

    def basic_price(self):
        return (self.duration * self.rental_type.price)

    def discount_price(self):
        return (self.basic_price() * (1 - self.FAMILY_DISCOUNT))
    
    @property
    def total_price(self):
        if self.has_family_discount():
            diff = self.bikes - 2
            if (diff > self.MAX_BIKES_DISCOUNT):
                diff = self.MAX_BIKES_DISCOUNT
            price = (self.basic_price() * (self.bikes - diff)) + (self.discount_price() * diff)
        else:
            price = self.basic_price() * self.bikes
        return price

    def __str__(self):
        ret = str(self.rental_type) + ' for ' + str(self.client) + ', '
        if self.has_family_discount():
            ret += 'with family discount, '
        ret += 'total price = ' + str(self.total_price)
        return ret
