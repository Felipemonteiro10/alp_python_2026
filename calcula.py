print(" as operação são: 1/2/3/4")
operaçao = int(input("digite a operação:"))

if operaçao <1 or operaçao >4: 
    print("Deu erro 404 meu mano")

else:
    print("upiiiiiiiiiiiii!!!")
    n1 = int(input("Digite o primeiro numero:"))
    n2 = int(input("Digite o segundo numero:"))

    if operaçao == 1:
        soma = n1 + n2
        print(f"resultado: {soma}")

    elif operaçao == 2:
        sub = n1 - n2
        print(f"resultado: {sub}")

    elif operaçao == 3:
        mul = n1 * n2
        print(f"Resultado: {mul}")

    elif operaçao == 4:
        div= n1 / n2
        print(f"Resultado: {div}")

    else:
        print(f"ebaaaaaaaa")