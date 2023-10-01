from my_module import Item, Shelf, PickList
import uuid, random

def get_random_shelf(shelf_list):
    if not shelf_list:
        return None
    random_index = random.randint(0, len(shelf_list) - 1)
    return shelf_list[random_index]

# Shelf 객체 생성
shelf_list = []
shelf_a = Shelf("A", 1)
shelf_list.append(shelf_a)
shelf_a2 = Shelf("A", 2)
shelf_list.append(shelf_a2)
shelf_a3 = Shelf("A", 3)
shelf_list.append(shelf_a3)
shelf_a4 = Shelf("A", 4)
shelf_list.append(shelf_a4)
shelf_a5 = Shelf("A", 5)
shelf_list.append(shelf_a5)
shelf_b = Shelf("B", 1)
shelf_list.append(shelf_b)
shelf_b2 = Shelf("B", 2)
shelf_list.append(shelf_b2)
shelf_b3 = Shelf("B", 3)
shelf_list.append(shelf_b3)
shelf_b4 = Shelf("B", 4)
shelf_list.append(shelf_b4)
shelf_b5 = Shelf("B", 5)
shelf_list.append(shelf_b5)
shelf_c = Shelf("C", 1)
shelf_list.append(shelf_c)
shelf_c2 = Shelf("C", 2)
shelf_list.append(shelf_c2)
shelf_c3 = Shelf("C", 3)
shelf_list.append(shelf_c3)
shelf_c4 = Shelf("C", 4)
shelf_list.append(shelf_c4)
shelf_c5 = Shelf("C", 5)
shelf_list.append(shelf_c5)

random_shelf = get_random_shelf(shelf_list)
# Item 객체 생성

item_1 = Item(uuid.uuid4(), "컴퓨터 마우스", 20000, get_random_shelf(shelf_list))
item_2 = Item(uuid.uuid4(), "노트북 가방", 35000, get_random_shelf(shelf_list))
item_3 = Item(uuid.uuid4(), "무선 키보드", 45000, get_random_shelf(shelf_list))
item_4 = Item(uuid.uuid4(), "스마트폰 케이스", 15000, get_random_shelf(shelf_list))
item_5 = Item(uuid.uuid4(), "무선 이어폰", 65000, get_random_shelf(shelf_list))
item_6 = Item(uuid.uuid4(), "헤드폰", 50000, get_random_shelf(shelf_list))
item_7 = Item(uuid.uuid4(), "세탁기", 550000, get_random_shelf(shelf_list))
item_8 = Item(uuid.uuid4(), "냉장고", 700000, get_random_shelf(shelf_list))
item_9 = Item(uuid.uuid4(), "전자레인지", 45000, get_random_shelf(shelf_list))
item_10 = Item(uuid.uuid4(), "청소기", 90000, get_random_shelf(shelf_list))
item_11 = Item(uuid.uuid4(), "디지털 카메라", 1200000, get_random_shelf(shelf_list))
item_12 = Item(uuid.uuid4(), "스피커", 55000, get_random_shelf(shelf_list))
item_13 = Item(uuid.uuid4(), "음식 조리기", 80000, get_random_shelf(shelf_list))
item_14 = Item(uuid.uuid4(), "에어컨", 900000, get_random_shelf(shelf_list))
item_15 = Item(uuid.uuid4(), "테이블 램프 ", 25000, get_random_shelf(shelf_list))
item_16 = Item(uuid.uuid4(), "서랍장", 130000, get_random_shelf(shelf_list))
item_17 = Item(uuid.uuid4(), "식탁 의자", 45000, get_random_shelf(shelf_list))
item_18 = Item(uuid.uuid4(), "소파", 350000, get_random_shelf(shelf_list))
item_19 = Item(uuid.uuid4(), "침대 시트", 60000, get_random_shelf(shelf_list))
item_20 = Item(uuid.uuid4(), "수영복", 35000, get_random_shelf(shelf_list))
item_21 = Item(uuid.uuid4(), "운동화", 80000, get_random_shelf(shelf_list))
item_22 = Item(uuid.uuid4(), "스니커즈", 70000, get_random_shelf(shelf_list))
item_23 = Item(uuid.uuid4(), "셔츠", 35000, get_random_shelf(shelf_list))
item_24 = Item(uuid.uuid4(), "원피스", 55000, get_random_shelf(shelf_list))
item_25 = Item(uuid.uuid4(), "청바지", 45000, get_random_shelf(shelf_list))
item_26 = Item(uuid.uuid4(), "모자", 15000, get_random_shelf(shelf_list))
item_27 = Item(uuid.uuid4(), "선글라스", 20000, get_random_shelf(shelf_list))
item_28 = Item(uuid.uuid4(), "화장품 세트", 75000, get_random_shelf(shelf_list))
item_29 = Item(uuid.uuid4(), "휴대용 충전기", 30000, get_random_shelf(shelf_list))


print(item_26.location.sector)

print(shelf_a3.items)