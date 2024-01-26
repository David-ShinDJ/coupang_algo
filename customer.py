
import re

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.credit = 0

    def charge_credit(self, amount):
        self.credit = amount

    def width_draw(self, amount):
        self.credit = self.credit - amount




