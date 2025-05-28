#Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros=[]
n = 0

for n in range(5):
    valor = int(input(f"Digite o numero {n + 1}: "))
    numeros.append(valor)

print(numeros)
soma = sum(numeros)
print(f"Soma: {soma}")
media = soma / len(numeros)
print(f"Media: {media}")