import dummy, my_module
# Product dummy 100 개 생성

## 출고량 100개 처리해보기
## 주문수량은 1개로 제한

import order, customer, product

## Customer 생성
some_customer = customer.Customer("신동준", "경기도 성남시 수정구 성남동 2382")
some_customer.charge_credit(100000)

## Product 생성
some_product = product.Product("아이폰 무선충전기", 23800)
some_product2 = product.Product("헬스스트랩", 28900)

## Order 생성
some_order = order.Order([some_product, some_product2], some_customer)

def print_object_properties(obj):
    for key, value in vars(obj).items():
        print(f"{key}: {value}")
print_object_properties(some_order)


