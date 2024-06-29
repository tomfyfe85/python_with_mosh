class Product:
    "Handling the price of a product"

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        "Returns the price"
        return self.__price

    @price.setter
    def price(self, value):
        "Ensures the price is a positive number"
        if value < 0:
            raise ValueError("Price must be a positive number")
        self.__price = value


product = Product(-20)
print(product.price)
