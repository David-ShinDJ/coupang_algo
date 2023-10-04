from my_module import Item, Shelf, PickList
import uuid

# Shelf 객체 생성
shelf_a = Shelf("A", 1)
shelf_a2 = Shelf("A", 2)
shelf_a3 = Shelf("A", 3)
shelf_a4 = Shelf("A", 4)
shelf_a5 = Shelf("A", 5)
shelf_b = Shelf("B", 1)
shelf_b2 = Shelf("B", 2)
shelf_b3 = Shelf("B", 3)
shelf_b4 = Shelf("B", 4)
shelf_b5 = Shelf("B", 5)
shelf_c = Shelf("C", 1)
shelf_c2 = Shelf("C", 2)
shelf_c3 = Shelf("C", 3)
shelf_c4 = Shelf("C", 4)
shelf_c5 = Shelf("C", 5)
# Item 객체 생성
item_1 = Item(uuid.uuid4(), "컴퓨터 마우스", 20000)
item_2 = Item(uuid.uuid4(), "노트북 가방", 35000)
item_3 = Item(uuid.uuid4(), "무선 키보드", 45000)
item_4 = Item(uuid.uuid4(), "스마트폰 케이스", 15000)
item_5 = Item(uuid.uuid4(), "무선 이어폰", 65000)
item_6 = Item(uuid.uuid4(), "헤드폰", 50000)
item_7 = Item(uuid.uuid4(), "세탁기", 550000)
item_8 = Item(uuid.uuid4(), "냉장고", 700000)
item_9 = Item(uuid.uuid4(), "전자레인지", 45000)
item_10 = Item(uuid.uuid4(), "청소기", 90000)
item_11 = Item(uuid.uuid4(), "디지털 카메라", 1200000)
item_12 = Item(uuid.uuid4(), "스피커", 55000)
item_13 = Item(uuid.uuid4(), "음식 조리기", 80000)
item_14 = Item(uuid.uuid4(), "에어컨", 900000)
item_15 = Item(uuid.uuid4(), "테이블 램프 ", 25000)
item_16 = Item(uuid.uuid4(), "서랍장", 130000)
item_17 = Item(uuid.uuid4(), "식탁 의자", 45000)
item_18 = Item(uuid.uuid4(), "소파", 350000)
item_19 = Item(uuid.uuid4(), "침대 시트", 60000)
item_20 = Item(uuid.uuid4(), "수영복", 35000)
item_21 = Item(uuid.uuid4(), "운동화", 80000)
item_22 = Item(uuid.uuid4(), "스니커즈", 70000)
item_23 = Item(uuid.uuid4(), "셔츠", 35000)
item_24 = Item(uuid.uuid4(), "원피스", 55000)
item_25 = Item(uuid.uuid4(), "청바지", 45000)
item_26 = Item(uuid.uuid4(), "모자", 15000)
item_27 = Item(uuid.uuid4(), "선글라스", 20000)
item_28 = Item(uuid.uuid4(), "화장품 세트", 75000)
item_29 = Item(uuid.uuid4(), "휴대용 충전기", 30000)

print(item_1.id)

print(hash("Hello"))
import hashlib

def generate_hash(data):
    # hashlib 모듈을 사용하여 SHA-256 해시 객체 생성
    sha256_hash = hashlib.sha256()

    # 데이터를 해시 객체에 업데이트
    sha256_hash.update(data.encode())

    # 해시 값을 얻음
    return sha256_hash.hexdigest()

# 예제 데이터에 대한 해시 생성
data = "Hello, World!"
hash_value = generate_hash(data)

# 해시 값을 출력
print("데이터 해시 값 (SHA-256):", hash_value)
