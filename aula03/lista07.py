#Faça um programa que leia 5 números e informe o maior número.
numeros = []

for i in range(5):
    numero = int(input(f"Digite o numero: "))
    numeros.append(numero)

print(f"{numeros}")

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(f"O maior numero e: {maior}")