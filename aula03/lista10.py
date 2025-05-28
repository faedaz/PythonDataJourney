#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
try:
    n1 = int(input("Digite o primeiro: "))
    n2 = int(input("Digite o segundo: "))
    inicio = min(n1, n2)
    fim = max(n1, n2)

    print(f"Inicio: {inicio}")
    print(f"Fim: {fim}")

    for i in range(inicio + 1, fim):
        if i % 2 == 0: 
            print(i)
except ValueError:
    print("Digite um valor valido!")

