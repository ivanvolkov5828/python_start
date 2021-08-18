prices = [57.8, 46.51, 97.4, 69.9, 34.5, 11.2, 22.53, 13.44, 19.1, 15.6]
my_list = []

# 1
for price in prices:
    rubles = int(price)
    kopecks = round(((price - rubles) * 100))
    my_list.append(f"{rubles} руб {kopecks} коп")
print(", ".join(my_list))
# 2
prices.sort()
id1 = id(prices)
for i in range(len(prices)):
    rubles = int(prices[i])
    kopecks = round(((prices[i] - rubles) * 100))
    prices[i] = f"{rubles} руб {kopecks} коп"
print(", ".join(prices))
id2 = id(prices)
print(id1 == id2)
# 3
prices_new = sorted(prices, reverse=True)
print(prices_new)
#4
print(sorted(prices_new[:5]))
