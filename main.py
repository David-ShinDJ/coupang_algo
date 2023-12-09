import dummy, my_module
# Product dummy 100 개 생성



products = dummy.generate_dummy_product(200)
product = my_module.Product("아이폰", 1240000)
order = my_module.Order(product, "서울")
order_list = my_module.OrderList()
order_list.add_order(order)


shelf = my_module.Shelf("A", 0)





