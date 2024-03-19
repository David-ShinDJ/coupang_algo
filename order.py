import time, re

class Order:

    def __init__(self, products, customer):
        self.products = products
        self.total_cost = sum((product.cost) for product in products)
        self.customer = customer
        self.region = self.get_region(customer.address)
        self.time = time.time()

        ## Order 생성시 Credit 차감
        self.customer.width_draw(self.total_cost)
    def get_region(self, address):

        # 지역분류 리스트정의
        delivery_category = ["서울","경기도","충청도","강원도","전라도","경상도","제주도","인천광역시","대전광역시","광주광역시","울산광역시","부산광역시"]

        # 지역분류 찾기위한 표현식
        pattern = r'\b(' + '|'.join(delivery_category) + r')\b'

        # 주소에서 지역분류를 검색
        match = re.search(pattern, address, re.IGNORECASE)

        if match:
            if match.group() in ['서울','서울특별시', '경기도']:
                return "수도권"
            elif match.group() in ['충청도', '충청남도', '충청북도']:
                return "충청"
            elif match.group() in ['강원도']:
                return "강원"
            elif match.group() in ['전라도', '전라남도', '전라북도']:
                return "전라"
            elif match.group() in ['경상도', '경상남도', '경상북도']:
                return "경상"
            elif match.group() in ['제주도', '제주특별시']:
                return "제주"
            elif match.group() in ['인천시', '인천광역시']:
                return "인천"
            elif match.group() in ['광주시', '광주광역시']:
                return "광주"
            elif match.group() in ['울산시', '울산광역시']:
                return "울산"
            elif match.group() in ['부산시', '부산광역시']:
                return "부산"
            else:
                return "해외"
        else:
            return "분류불가"