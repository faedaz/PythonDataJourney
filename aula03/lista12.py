'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
'''
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    numero = int(input("Digite o número de 1 a 10 para ver a tabuada: "))

    
    for i in tabuada:
        print(f"{numero} x {i} = {numero * i}")
    
except ValueError:
    print("Digite um valor válido!")
