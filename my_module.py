import hash, time, random
# TODO: 실제 직원이 토트에 물건을 담아보기
# 출고시스템부터 설계 -> 집품 최소이동 단위로 설계하기!

class Customer:
    def __init__(self, info):
        self.info = info
        self.sub = False

class Tote:
    def __init__(self):
        self.number = self.tote_number()

    def tote_number(self):
        # "xx" 부분을 무작위 숫자로 채우기
        number = str(random.randint(0, 9))
        number2 = str(random.randint(0, 9))
        number3 = str(random.randint(0, 9))
        number4 = str(random.randint(0, 9))
        number5 = str(random.randint(0, 9))

        return f"136-RCRT41-{number}{number2}-{number3}{number4}{number5}"


# 직원
class Employee:
    def __init__(self, name, employee_number, occupation):
        self.name = name
        self.employee_number = employee_number
        self.occupation = occupation
class Picker(Employee):
    def __init__(self, tote, pda):
        self.tote = tote
        self.pda = pda

class Delivery(Employee):
    def __init__(self, line, pda):
        self.line = line
        self.pda = pda


class PDA:
    def __init__(self, machine_number, work_type):
        self.machine_number = machine_number
        self.work_type = work_type

class Inventory:
    def __init__(self, product_data):
        self.product_data = product_data
        

class Shelf:
    def __init__(self, sector, number):
        self.sector = sector  # A~C
        self.number = number  # 1~15
        self.products = []  # item max 28

    def add_item(self, product):
        self.products.append(product)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.barcode = hash.hash_name(name)
        self.price = price

class Order:
    def __init__(self, product, customer):
        self.product = product
        self.customer = customer
        self.time = time.time()
        self.region = random.randint(0, 11)


# TODO: Order 들어올떄 마감값에 따라서 리스트앞에 넣는 함수 구현하기
# sort_order function Order.time값에 따라 앞에 넣어주는함수 힙구조?
class OrderList:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
            print(f"{order.product.name} is removed")

    def sort_order(self):
        self.orders = sorted(self.orders, key=lambda x: x.time)

    def get_order_list(self):
        for order in self.orders:
            print(order.product.name)
    def get_order_time(self):
        for order in self.orders:
            print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(order.time)))
    def get_order_name(self):
        for order in self.orders:
            print(order.product.name)

class PickList:

