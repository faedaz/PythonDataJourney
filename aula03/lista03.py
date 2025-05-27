'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
'''

# Coleta do nome
while True:
    nome = input("Digite seu nome: ")
    if len(nome) < 3:
        print("O nome precisa ter mais de 3 caracteres!")
        continue
    else:
        break

# Coleta da idade
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade <= 0 or idade >= 150:
            print("Digite uma idade válida!")
        else:
            break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# Coleta do salário
while True:
    try:
        salario = float(input("Digite o salário: "))
        if salario < 0:
            print("Digite um valor válido para o salário!")
        else:
            break
    except ValueError:
        print("Entrada inválida! Digite um número (use ponto em vez de vírgula, se necessário).")

#coleta do sexo
while True:
    sexo = input("Digite 'f' para feminino e 'm' masculino: ")
    if sexo == "f":
        sexo = "feminino"
        break
    elif sexo == "m":
        sexo = "masculino"
        break
    else:
        print("Digite um valor valido!")
        continue

# Print final em uma linha só
print(f"\nCadastro completo: Nome: {nome}, Idade: {idade}, Salário: R$ {salario:.2f}, sexo: {sexo}")
