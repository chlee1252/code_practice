money = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]

result = 0
for coin in coins:
    if money < 0:
        break
    if money >= coin:
        result += money // coin
        money %= coin

print(result)