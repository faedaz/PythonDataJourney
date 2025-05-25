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

# 5. Ano bissexto
# Peça um ano e diga se ele é bissexto.
# (Dica: divisível por 4 e não por 100, exceto se também for divisível por 400.)

# 6. Acesso permitido
# Peça uma senha e diga se ela está correta (ex: a senha correta é "1234").

# 7. Verificar faixa etária
# Peça a idade de uma pessoa e diga se ela é:
# criança (0-12), adolescente (13-17), adulta (18-64) ou idosa (65+).

# 8. Aprovado ou reprovado
# Solicite a média de um aluno e diga se ele foi aprovado (nota ≥ 7),
# em recuperação (nota entre 5 e 6.9) ou reprovado (nota < 5).

# 9. Calculadora simples
# Peça dois números e uma operação (+, -, *, /) e realize a operação correta.
# Use if para cada operação.

# 10. Desconto por valor de compra
# Peça o valor de uma compra. 
# Se for maior que R$100, aplique 10% de desconto e mostre o valor final.
