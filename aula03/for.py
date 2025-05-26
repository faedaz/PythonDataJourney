#Escreva um programa que use um loop for para imprimir todos os números pares de 0 a 20.

for contador in range(0, 21, 2):
    print(contador)

#Peça ao usuário um número e use um loop for para exibir a tabuada desse número (de 1 a 10).

numero = int(input("Digite um numero: "))

for contador in range(1, 11):
    print(numero * contador)

#Crie uma lista de números (ex: [5, 10, 15, 20]) e use um loop for para calcular a soma de todos os elementos.

numeros = [5, 10, 15, 20]  # Passo 1
soma = 0                   # Passo 2

for i in numeros:     # Passo 3
    soma += i         # Passo 4

print("A soma dos números é:", soma)  # Passo 5

#Faça um programa que use um loop for para fazer uma contagem regressiva de 10 até 1 e depois imprima "Fogo!".

contagem_regressiva = 10

for i in range(contagem_regressiva, 0, -1):
    print(f"{i}")
print("Fogo")

for i in range(0, 51, 2):
    print(i)

#faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 ate 500

soma = 0
for numero in range(1, 501, 2):  # Percorre só os ímpares (pulando de 2 em 2)
    if numero % 3 == 0:          # Verifica se é múltiplo de 3
        soma += numero
print(f"Soma dos ímpares múltiplos de 3 (1-500): {soma}")