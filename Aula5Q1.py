import random
print("Rifa")
print("-"*50)
print("Dígite encerrar para acabar a rifa")
print("-"*50)
part = []
while True:
    pes = str(input("Dígite o nome: "))
    if pes.lower() == "encerrar":
        break
    part.append(pes)
venc = random.choice(part)
print("Encerrando a Rifa")
print(f"O vencedor da rifa é {venc}")