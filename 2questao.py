pares = 0
for cont in range (10):
    num = int(input("digite os numeros:"))
    if num % 2 ==0 :
        pares += 1
        print(f"tem {pares} é par")
    else:
        print("é impar")
print("deu certo")