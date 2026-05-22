import os
for tentativa in range(1,4):
    usuario = input("usuário: ")
    senha = input("senha: ")
    if usuario == "aluno" and senha == "12345":
        print("acesso liberado")
        break
    else:
        print("tente novamente!")
        os.system("clean")
if tentativa == 3:
    print("ja tentou 3 vezes, seu burro")