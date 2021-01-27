# Using list here: in this searching for date->price complexity is O(N)

stock_prices_list = []
with open('stock_prices.csv')as f:
    for line in f:
        token = line.split(',')
        day = token[0]
        price = float(token[1])
        stock_prices_list.append([day, price])
print(stock_prices_list)

for line in stock_prices_list:
    if line[0] == 'May 1':
        print(line[1])

# Using Hashmap: Dictionary is Python specific implementation using Hashmap only->Complexity O(1)
stock_prices_dict = {}
with open('stock_prices.csv')as f:
    for line in f:
        token = line.split(',')
        day = token[0]
        price = token[1]
        stock_prices_dict[day] = float(price)  # float()will remove /n from the price values
print(stock_prices_dict)

print(stock_prices_dict['Nov 27'])
