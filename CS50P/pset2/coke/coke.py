coins = [25, 10, 5]
total = 0

while total < 50:
    coin = int(input("Insert coin: "))
    if coin in coins:
        total += coin
    if total < 50:
        print("Amount Due:", 50 - total)

print("Change Owed:", total - 50)
