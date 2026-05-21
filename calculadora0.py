print(" Calculadora de números reais ")
print("0. sair")
print("1. soma")
print("2. subtração")
print("3. multiplicação")
print("4. divisão")
opcao = int(input("Escolha a operação desejada:"))
while opcao != 0:
    if opcao == 0:
        print("saindo da calculadora")
        break
    num1 = float(input("Digite o número 1:"))
    num2 = float(input("Digite o número 2:"))
    if opcao == 1:
        resultado1 = num1 + num2
        print("O resultado da soma é:", resultado1)
    elif opcao == 2:
        resultado2 = num1 - num2
        print("O resultado da subtração é:", resultado2)
    elif opcao == 3:
        resultado3 = num1 * num2
        print("O resultado da multiplicação é:", resultado3)
    elif opcao == 4:
        resultado4 = num1 / num2
        print("O resultado da divisão é:", resultado4)
    else:   
        print("Opção não existe")