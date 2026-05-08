num = int(input("digite o numero:"))

if num <= 0:
    print("Digite um numero maior que zero")
    
elif num %2 == 0:
    print(f"numero é par, ao qudrado é: {num**2}")

else:
    print(f"numero é impar, ao cubo é: {num**3}")