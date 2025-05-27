##Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome = input("Digite o seu nome: ").lower()
    senha = input("Digite sua senha: ").lower()
    if nome == senha:
        print("Digite novamente, nome e senha nao podem ser iguais!")
    else:
        break