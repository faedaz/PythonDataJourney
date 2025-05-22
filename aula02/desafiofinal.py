CONSTANTE_BONUS = 1000

#nome
while True:
    nome = input("Digite o nome: ")
    if nome.replace(" ", "").isalpha():
        break
    else:
        print("Digite um nome válido (somente letras)")

#salario
while True:
    try:
        salario_usuario = float(input("Digite o salario: "))
        break
    except ValueError:
        print("Voce digiou um valor inváldio")

#bonus
while True:
    try:
        bonus_usuario = float(input("Digite o seu bonus: "))
        break
    except ValueError:
        print("Voce digitou um valor inválido!")

valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario
print(f"O valor final do bonus sera: {valor_bonus}")
