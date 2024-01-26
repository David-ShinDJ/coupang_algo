import time, re

class Order:

    def __init__(self, products, customer):
        self.products = products
        self.total_cost = sum(product.cost for product in products)
        self.customer = customer
        self.region = self.get_region(customer.address)
        self.time = time.time()
    def get_region(self, address):

        # 지역분류 리스트정의
        delivery_category = ["서울","경기도","충청도","강원도","전라도","경상도","제주도","인천광역시","대전광역시","광주광역시","울산광역시","부산광역시"]

        # 지역분류 찾기위한 표현식
        pattern = r'\b(' + '|'.join(delivery_category) + r')\b'

        # 주소에서 지역분류를 검색
        match = re.search(pattern, address, re.IGNORECASE)

        if match:
            if match == '서울' or "경기도":
                return "수도권"
            elif match == '충청도':
                return "충청"
            elif match == '강원도':
                return "강원"
            elif match == '전라도':
                return "전라"
            elif match == '경상도':
                return "경상"
            elif match == '제주도':
                return "제주"
            elif match == '인천광역시':
                return "인천"
            elif match == '광주광역시':
                return "광주"
            elif match == '울산광역시':
                return "울산"
            elif match == '부산광역시':
                return "부산"
            else:
                return "해외"
        else:
            return "분류불가"