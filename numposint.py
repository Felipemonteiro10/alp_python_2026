num1 = int(input("Digite um número positivo: "))
num2 = 0
while num1 > 0:
    num1 = int(input("Digite um número positivo: "))
    if num1 < 0:
        print(f"a soma é: {num2}")
        print(f"a média aritmética é: {num2/2}")
        print(f"o maior número é: {num2}")
    num2 = num1 + num2



