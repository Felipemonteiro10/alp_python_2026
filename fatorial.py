
def fator(n):
    fat = 1

    for i in range(1, n + 1):
        fat = fat * i

    return fat
    
print("digite o numero zero para sair")

n = int(input("Digite um número: "))

while n != 0:
    print("a fatorial desse numero é =", fator(n))

    n = int(input("Digite outro número : "))

print("Fim do programa!")
