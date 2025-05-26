#crie uma lista com 4 numeros inteiros e mostre a soma apenas daqueles que forem pares.

lista = [1, 2, 4, 9]

armazenar = 0

for numero in lista:
    if numero % 2 == 0:
        armazenar = armazenar + numero
        print(f"{armazenar}")

#desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.

p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))

for n in range(1, 11):
    termo = p + (n - 1) * r
    print(termo)