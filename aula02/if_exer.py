
try:
    numero = int(input("Digite um numero inteiro: "))
    if numero < 0:
        print("Numero negativo!")
    elif numero == 0:
        print("Numero 0")
    else:
        print("Numero positivo!")
except ValueError:
    print("Digite um valor valido!")            