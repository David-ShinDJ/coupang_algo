import hash, csv

class Product:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.barcode = hash.hash_name(name)

    def __str__(self):
        return f"Product(Name: {self.name}, Cost: {self.cost})"

