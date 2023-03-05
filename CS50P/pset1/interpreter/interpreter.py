[x, y, z] = input("Expression: ").strip().split()

x = float(x)
z = float(z)
if y == "+":
    res = x + z
elif y == "-":
    res = x - z
elif y == "*":
    res = x * z
elif y == "/":
    res = x / z
else:
    res = 0

res = round(res, 1)
print(res)
