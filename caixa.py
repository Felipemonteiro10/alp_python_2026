tenta = 3
nome = input("digite seu nome: ")
senha = input("digite sua senha: ")
while senha != "123456" and tenta > 1:
    tenta -= 1
    print(f"senha incorreta, você tem {tenta} tentativas")
    senha = input("digite sua senha: ")
if senha == "123456":
    print(f"olá {nome}, seja bem-vindo ao nosso banco")
else:
    print("sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
