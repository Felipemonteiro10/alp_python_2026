senha = int(input("digite a senha:"))

while senha!= 12345:
    print("acesso negado")
    senha = int(input("digite novamente:"))
    if senha == 12345: 
        print("deu certo")