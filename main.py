from my_module import Item, OrderList
## 객체지향 코드예시
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greeting(self):
        print(f"Hi My Name is {self.name}, and I am {self.age} years old")


# 테스트
David = User("David", 29)
July = User("July", 25)

David.greeting()
July.greeting()

First_Item = Item(1, "ADD", 1)

First_Order = OrderList([First_Item])

First_Order.read()

