remedio = 0
for cont in range(1,6):
    nome = input("digite o nome do medicamento:")
    preco = float(input("digite o preço do medicamento:"))
    remedio += preco
print(f"o nome do medicamento é {nome} e o preço é {preco}, sendo a mais barata")
