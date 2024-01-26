import hash


class Product:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.barcode = hash.hash_name(name)
