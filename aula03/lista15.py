#Peça ao usuário três números inteiros e exiba o maior deles.

numeros = []
try:
    #preenchendo uma lista
    for n in range(0, 3, 1): 
        n1 = int(input("Digite o numero: "))
        numeros.append(n1)
    
    print(numeros)
    print(f"O maior numero e: {max(numeros)}")
except ValueError:
    print("Digite um valor valido!")