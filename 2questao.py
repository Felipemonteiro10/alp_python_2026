pares = 0
impars = 0
for cont in range (1,11):
    num = int(input("digite os numeros:"))
    if num % 2 ==0 :
        pares += 1
    else:
        impars +=1
print(f"tem {pares} é par")
print(f"tem {impars} é impar")