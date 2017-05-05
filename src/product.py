#.

class Product(object):
    """docstring for Product"""

    def __init__(self, price, title):
        self.__price = price
        self.__title = title

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return 1
