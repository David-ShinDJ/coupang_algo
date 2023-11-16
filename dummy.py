from faker import Faker
import random
import time
import my_module


def generate_dummy_product(num_products=100):
    fake = Faker()
    dummy_product = []

    for _ in range(num_products):
        name = fake.word()
        price = round(random.uniform(10, 1000), 2)

        product = my_module.Product(name, price)
        dummy_product.append(product)

    return dummy_product

def generate_dummy_order(products):
    fake = Faker()
    dummy_order = []

    for product in products:
        order_product = product
        order_region = "서울"

        order = my_module.Order(order_product, order_region)
        order.time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(round(random.uniform(int(time.time()) - 3600 * 12, int(time.time())), 0)))
        dummy_order.append(order)

    return dummy_order

