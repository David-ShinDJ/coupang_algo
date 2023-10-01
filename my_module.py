import uuid  # uuid 모듈을 추가해야 합니다.

class Shelf:
    def __init__(self, sector, number):
        self.sector = sector
        self.number = number
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class Item:
    def __init__(self, id, name, price, shelf):
        self.id = id
        self.name = name
        self.price = price
        self.location = shelf  # shelf.sector + str(shelf.number) 대신 shelf 객체를 직접 할당

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