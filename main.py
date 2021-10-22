import math
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))

if x1 == x2 and x1 == x3 or y1 == y2 and y1 == y3:
    print("Uchburchak yasab bo`lmaydi")
else:
    a = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    b = math.sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2))
    c = math.sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print(a)


