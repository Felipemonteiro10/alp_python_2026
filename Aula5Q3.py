usuarios = {}
print("Digite encerrar para acabar.")
print("-"*50)
while True:
    usuario = input("Cadastre seu usuário: ")
    if usuario.lower() == "encerrar":
        break
    senha = input("Cadastre sua senha: ")
    if senha.lower() == "encerrar":
        break
    usuarios[usuario] = senha
    print("Cadastro feito")
print("Encerrando cadastro")
print("Faça login")
loginusu = input("Digite seu usuário: ")
loginsen = input("Digite sua senha: ")
if loginusu in usuarios:
    if loginsen == usuarios[loginusu]:
        print(f"Bem vindo {loginusu}")
    else:
        print("Senha errada")
else:
    print("Usuário invalido")