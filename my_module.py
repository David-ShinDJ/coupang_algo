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
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.region = region



# TODO: Order 들어올떄 마감값에 따라서 리스트앞에 넣는 함수 구현하기
# TODO: First In First Out 구현하기위해서 hip 구조를 사용?
# sort_order function Order.time값에 따라 앞에 넣어주는함수 힙구조?
# 
def string_to_timestamp(date_string):
    # 주어진 문자열을 시간 구조체로 변환
    time_struct = time.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    # 시간 구조체를 timestamp로 변환
    timestamp = time.mktime(time_struct)

    return int(timestamp)
def get_timestamp(order):
    return string_to_timestamp(order.time)
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
        sorted_order = sorted(self.orders, key=get_timestamp)
        print(sorted_order)

    def get_order_list(self):
        for order in self.orders:
            print(order.product.name)



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
