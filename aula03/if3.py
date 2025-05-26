# 1. Número positivo ou negativo
# Peça ao usuário para digitar um número e diga se ele é positivo, negativo ou zero.
numero = float(input("Digite o número: "))

if numero < 0:
    print("Negativo")
elif numero > 0:
    print("Positivo")
else:
    print("Zero")

# 2. Par ou ímpar
# Peça ao usuário um número e informe se ele é par ou ímpar.

numero2 = float(input("Digite o numero: "))

if numero2 % 2 == 0:
    print("par")
else:
    print("impar")

# 3. Maior de dois números
# Solicite dois números e informe qual é o maior.
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if n1 > n2:
    print("Primeiro valor e o maior!")
elif n2 > n1:
    print("O segundo valor e o maior!")
else:
    print("Valores iguais")


# 4. Triângulo válido
# Peça três lados e verifique se eles podem formar um triângulo 
# (dica: a soma de dois lados deve ser maior que o terceiro).
t1 = int(input("Digite o primeiro lado: "))
t2 = int(input("Digite o segundo lado: "))
t3 = int(input("Digite o terceiro lado: "))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print("Triângulo!")
else:
    print("Não é triângulo!")

#Exercício 1: Verificar se um elemento existe em uma lista
#Crie uma lista de números e peça ao usuário para digitar um número. Verifique se o número está na #lista e imprima uma mensagem correspondente.

lista_numero = [10,  20, 30, 40, 50, 60, 70, 80, 90, 100]
numero = int(input("Digite o numero: "))

if numero in lista_numero:
    print("Numero encontrado!")
else:
    print("Numero nao encontrado!")