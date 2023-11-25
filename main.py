import dummy, my_module
# Product dummy 100 개 생성


dummy_products = dummy.generate_dummy_product(200)
dummy_orders = dummy.generate_dummy_order(dummy_products)


order_list = my_module.OrderList()

for order in dummy_orders:
    order_list.add_order(order)

order_list.sort_order()
print(len(order_list.orders))
order_list.get_order_time()
