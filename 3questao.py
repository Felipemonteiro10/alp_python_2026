tentativa = 3
usuario = input("Digite o usuario:")
senha = input("Digite a senha:")
while (usuario !="aluno" or senha != "12345") and tentativa >1:
    tentativa-= 1
    print(f"Senha ou usuário erradas ({tentativa} restantes)")
    usuario=input("Digite novamente o usuario:")
    senha=input("Digite novamente a senha:")
if usuario=="aluno" or senha== "12345":
    print("acesso liberado")
else:
    print("bloqueado")