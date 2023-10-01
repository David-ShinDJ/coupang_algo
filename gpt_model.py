class Item:
    def __init__(self, name, price, quantity):
        self.name = name  # 아이템 이름
        self.price = price  # 아이템 가격
        self.quantity = quantity  # 주문 수량

    def calculate_total(self):
        return self.price * self.quantity  # 총 가격 계산

class OrderList:
    def __init__(self):
        self.items = []  # 주문 목록에 포함된 아이템 리스트

    def add_item(self, item):
        self.items.append(item)  # 아이템 추가

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)  # 아이템 제거

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_total()  # 모든 아이템의 총 가격 합산
        return total

# 예제 사용
item1 = Item("커피", 5.99, 2)
item2 = Item("차", 3.49, 3)
item3 = Item("과자", 2.99, 4)

order = OrderList()
order.add_item(item1)
order.add_item(item2)
order.add_item(item3)

print("주문 목록:")
for item in order.items:
    print(f"{item.name}: 가격 - ${item.price}, 수량 - {item.quantity}, 총 가격 - ${item.calculate_total()}")

print(f"총 주문 가격: ${order.calculate_total()}")