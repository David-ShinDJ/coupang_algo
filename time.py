import time

현재_시간 = time.localtime()
현재_시간 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("현재 시간:", 현재_시간)