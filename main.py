import dummy, my_module, csv, logistics_center, worker, inventory
# Product dummy 100 개 생성

## 출고량 100개 처리해보기
## 주문수량은 1개로 제한

import order, customer, product


## Customer 생성

some_customer = customer.Customer("신동준", "경기도 성남시 수정구 성남동 2382")
some_customer.charge_credit(100000)
some_customer2 = customer.Customer("아무개", "충청도 연수구 주안동 1203")
some_customer2.charge_credit(100000)
## Product 생성
products = []
with open("product_sample.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        some_product = product.Product(row[0], int((row[1])))
        products.append(some_product)

## Order 생성
some_order = order.Order([products[0], products[1]], some_customer)
some_order2 = order.Order([products[2], products[3]], some_customer2)
def print_object_properties(obj):
    for key, value in vars(obj).items():
        print(f"{key}: {value}")
print_object_properties(some_order)
print(some_customer.credit)
print_object_properties(some_order2)


## TODO: LogisticCenter 생성하기 모든 클래스 연결해서 main 작성하기

inventory_data = inventory.InventoryData




