
# Task 1: Create Base Product Class

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def show_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}\n")

# Task 2: Implement Subclasses for Specific Products

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def show_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Author: {self.author}\n")

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def show_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Specs: {self.specs}\n")

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size        

    def show_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Size: {self.size}\n")


# Task 3: Override Display Method in Subclasses

# Task 4: Test Product Catalog Functionality

book = Book("feauhngfe", "Dune", 5.99, "Frank Herbert")
electronic = Electronic("jiefgwapoij", "Camera", 350.00, "Zoom")
clothing = Clothing("oiipjafwe", "T-shirt", 15.95, "Medium")

book.show_details()
electronic.show_details()
book.show_details()