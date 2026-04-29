print("As opções são: 1. Média ponderada." \
"2. Quadrado da soma dos 2 números" \
".3. Cubo do menor número")

opçao = int(input("escolhha entre a opções de 1 a 3: "))

if opçao <1 or opçao >3:
    print("opção não exite")

else:
    print("Agora escolha dois numeros positivos")
    n1 = int(input("Digite o primeiro numero: "))
    if n1 <= 0:
        print("não pode")
    n2 = int(input("Digite o segundo numero: "))
    if n2 <= 0:
        print("não pode")

    if opçao == 1:
        print(f"a média ponderada entre os numeros é: {(n1*2 + n2*3)/(2+3)} ")
    elif opçao == 2:
        print(f"o quadrado da soma é: {(n1 + n2)**2}")
    elif opçao == 3:
        if n1 > n2:
            print("cubo do menor numero é: {(n2)**3}")
        elif n1 < n2:
            print(f"cubo do menor numero é: {(n1)**3}")
        elif n1==n2:
            print("os dois numeros são iguais")
        else:
            print("seu valor deu certo")
    else:
        print("seu valor foi encontrado")