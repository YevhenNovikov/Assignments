class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author
    
    def read(self):
        print(f"Book {self.name}, author: {self.author}, - price: {self.price}. Quantity: {self.quantity}")

book1 = Book('"The Financier"', 20, 100, "Theodore Herman Albert Dreiser")
book1.read()