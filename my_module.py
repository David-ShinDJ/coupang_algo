import uuid  # uuid 모듈을 추가해야 합니다.

# 시스템 설계 -> 원하는 기능 구현 -> 실제쿠팡에서 집품을 하는 알고리즘을 기준으로 설계
# 모듈설계 -> 각자의 독립적인 모듈을 생성후에 연결하는방식으로 설계
# 데이터설계 -> 관계형데이터베이스기반 -> 더미데이터생성후 유닛테스트
# 각 설계를 어떻게 연결할지에 대해서 설계필요
# @ 실제존재하는것 기반으로 설계진행 ! 확장성을 고려해서 설계진행!


class Shelf:
    def __init__(self, sector, number):
        self.sector = sector  # A~C
        self.number = number  # 1~5
        self.items = []  # item 4개

    def add_item(self, item):
        self.items.append(item)

class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
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