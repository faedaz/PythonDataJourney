#Peça ao usuário um número e exiba uma mensagem dizendo se ele é positivo.
try:
    lista_n = []
    n1 = int(input("Digite n1: "))
    lista_n.append(n1)

    for numero in lista_n:
        if numero >= 0:
            positivo = lista_n
            print(f"Numero {lista_n}")
        else:
            negativo = lista_n
            print(f"Numero: {lista_n}")
except ValueError:
    print("Digite um numero valido!")

print(lista_n)

