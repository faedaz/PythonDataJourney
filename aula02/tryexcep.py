#é uma forma de testar sem crashar o arquivo
try:
    n1 = int(input("Digite o número: "))
    n2 = int(input("Digite o outro: "))
    print(f"A divisao sera: {n1//n2}")
except:
    print("Erro!")