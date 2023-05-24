import math

a = 4
b = 7
c = 4

a = math.sqrt(b ** 2 + c ** 2 - 2 * b * c * math.cos(a))
b = math.sqrt(a ** 2 + c ** 2 - 2 * a * c * math.cos(b))
c = math.sqrt(b ** 2 + a ** 2 - 2 * b * a * math.cos(c))

print(a)
print(b)
print(c)
