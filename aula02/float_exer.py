
#Números de Ponto Flutuante (float)
#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n_media = float(input("Digite: "))
n_media2 = float(input("Digite o outro número: "))
media = (n_media + n_media2) / 2
print(f"A media é {media}")
#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
expoente = float(input("Digite o expoente: "))
base = float(input("Digite a base: "))
potencia = base ** expoente
print(f"A potencia é {potencia}")
#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em celsius: "))
fah = (celsius * 9/5) + 32
print(f"A temperatura em fahrenheit será: {fah}")
#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio: "))
area = 3.14 * raio ** 2
print(f"A area é {area}")
