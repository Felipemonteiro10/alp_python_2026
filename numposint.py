num1 = 1
num2 = 0
cont = 0
maior = 0
while num1 > 0:
    num1 = int(input("Digite um número positivo: "))
    if num1 > 0:
        num2 += num1 
        cont += 1
    if num1 > maior:
        maior = num1
print(f"a soma é: {num2}")
print(f"a média aritmética é: {num2/cont}")
print(f"o maior número é: {maior}")




