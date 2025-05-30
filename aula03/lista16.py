#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.


numeros = []
par = 0
impar = 0

for i in range(0, 10):
    numero = int(input(f"Digite o numero {i+1}: "))
    numeros.append(numero)
    
    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    
print(numeros)
print(f"Pares: {par}")
print(f"Impares: {impar}")