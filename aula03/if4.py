#Crie um dicionário com nomes e idades. Peça ao usuário para digitar um nome e verifique se a pessoa é maior de 18 anos.

registro = {'Matheus': 30, 'Enzo': 12, 'Paulinho': 26}
nome = input("Digite o nome: ").capitalize()

if nome in registro:
    if registro[nome] >= 18:
        print("Maior de idade!")
    else:
        print("Menor de idade!")


#Dada uma tupla de números, verifique se o primeiro elemento é maior que o último e imprima o resultado.

numeros_tupla = (10, 22, 30, 34, 99, 2)

if numeros_tupla[0] > numeros_tupla[-1]:
    print("O primeiro e maior!")
elif numeros_tupla[0] < numeros_tupla[-1]:
    print("O ultimo e maior!")
else:
    print("Sao iguais!")

#Crie um dicionário de usuários e senhas. Peça ao usuário para digitar login e senha, e #verifique se estão corretos.

login = {'mathe': 'AgJ99', 'Us09': 'Lkjh', 'Kjh': 'G29*kl'}
login_usr = input("Digite o login: ")
senha_usr = input("Digite a senha: ")

if login_usr in login:
    if login[login_usr] == senha_usr:
        print("Acesso permitido!")
    else:
        print("Senha incorreta. Acesso negado!")
else:
    print("Acesso negado!")        


#Dada uma lista de produtos e seus preços, imprima os produtos categorizados como "Barato" (preço < 50), "Médio" (50 ≤ preço < 100) ou "Caro" (preço ≥ 100).
produtos = {
    "Caneta": 2.50,
    "Caderno": 35.00,
    "Monitor": 450.00
}

for nome, preco in produtos.items():
    if preco < 50:
        categoria = "Barato"
    elif preco < 100:
        categoria = "Médio"
    else:
        categoria = "Caro"
    print(f"{nome}: R${preco:.2f} → {categoria}")