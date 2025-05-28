#Altere o programa anterior para mostrar no final a soma dos números.
lista_soma = []
try:
    n1 = int(input("Digite o primeiro: "))
    n2 = int(input("Digite o segundo: "))
    inicio = min(n1, n2)
    fim = max(n1, n2)

    print(f"Inicio: {inicio}")
    print(f"Fim: {fim}")

    for numero in range(inicio + 1, fim):
        if numero % 2 == 0: 
            print(numero)
            
    lista_soma.append(numero)
    soma = sum(lista_soma)           
    print(f"A soma e: {soma}")        
except ValueError:
    print("Digite um valor valido!")