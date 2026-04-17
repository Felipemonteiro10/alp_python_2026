

peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

imc = peso/altura**2

print(f"valor do imc é: {imc:.2f}")

if imc < 18.5: 
    print("Magreza")

elif imc <= 24.9:
    print("Peso normal")

elif imc <= 29.9: 
    print("Sobrepeso")

elif imc <= 39.9:
    print("Obesidade")

else:
    print("Obesidade grave")
