import hash, time
# 출고시스템부터 설계 -> 집품 최소이동 단위로 설계하기!

# 직원
class Employee:
    def __init__(self, name, employee_number, occupation):
        self.name = name
        self.employee_number = employee_number
        self.occupation = occupation

# PDA

class PDA:
    def __init__(self, machine_number, work_type):
        self.machine_number = machine_number
        self.work_type = work_type

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
    def __init__(self, product, region):
        self.product = product
        self.time = time.time()
        self.region = region



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


class PickList:
    def __init__(self):
        self.items = []

    def pick_item(self, item):
        self.items.append(item)
        print(f"The Item: {item.name} is Picked")  # item을 출력할 때 item.name을 사용
        item.location.items.remove(item)
    def put_item(self, item):
        self.items.remove(item)
        item.location.items.append(item)
        print(f"The Item: {item.name} is put on Shelf")  # item을 출력할 때 item.name을 사용

    def read(self):
        for item in self.items:
            print(f"{item.name}")
