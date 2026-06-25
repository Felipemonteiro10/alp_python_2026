soma = 0
menorp = 0
menorn = 0
preco = 0
for cont in range(5):
    nome = input("digite o nome do medicamento:")
    preco = float(input("digite o preço do medicamento:"))
    soma += preco
    if cont== 0:
        menorn=nome
        menorp=preco
    elif preco < menorp:
        menorn=nome
        menorp=preco
print(f"a media desses preços é: {soma/5}")
print(f"o nome do medicamento é {menorn} e o preço é {menorp}, sendo a mais barata")

