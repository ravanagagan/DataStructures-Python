wmt_stock_price_queue = []

wmt_stock_price_queue.insert(0, 131.0)
wmt_stock_price_queue.insert(0, 132.0)
wmt_stock_price_queue.insert(0, 133.0)

# 5 - Queue will fallow FIFO so whenever we insert element in 0th position the previous element will move forward
# List will fallow Dynamic memory allocation scheme so memory    allocation problem will occur
print(wmt_stock_price_queue)

print(wmt_stock_price_queue.pop())  # 131.0
print(wmt_stock_price_queue.pop())  # 132.0
print(wmt_stock_price_queue.pop())  # 133.0
# print(wmt_stock_price_queue.pop())  # Error
