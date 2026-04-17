from math import sqrt

x1 = int(input("digite o valor de x1: "))
y1 = int(input("digite o valor de y1: "))
x2 = int(input("digite o valor de x2: "))
y2 = int(input("digite o valor de y2: "))

d = sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"o valor d distancia entre o dois pontos é: {d:.2f}")