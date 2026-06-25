usuario = []
senha = []
print("Digite encerrar para finalizar.")
print("-"*50)
while True:
    cadastrousu = input("Cadastre seu usuário: ")
    if cadastrousu.lower() == "encerrar":
        break
    cadastrosen = input("Cadastre sua senha: ")
    if cadastrosen.lower() == "encerrar":
        break
    usuario.append(cadastrousu)
    senha.append(cadastrosen)
    print("Cadastro feito")
print("faça login")
loginusu = input("Digite seu usuário: ")
loginsen = input("Digite sua senha: ")
if loginusu in usuario:
    indice = usuario.index(loginusu)
    if loginsen == senha[indice]:
        print(f"Bem vindo {loginusu}")
    else: print("Senha errada")
else: print("Usuário invalido")