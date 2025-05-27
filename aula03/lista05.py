#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


populacao = {}
populacao["A"] = int(input("Digite o numero de habitantes do pais A: "))
populacao["B"] = int(input("Digite o numero de habitantes do pais B: "))
print(populacao)

crescimento = {}
crescimento["taxa_A"] = float(input("Digite a taxa de crescimento do pais A: "))
crescimento["taxa_B"] = float(input("Digite a taxa de crescimento do pais B: "))
print(crescimento)

contador_de_anos = 0

while populacao["A"] <= populacao["B"]:
            populacao["A"] = int(populacao["A"] * (1 + crescimento["A"] / 100))
            populacao["B"] = int(populacao["B"] * (1 + crescimento["B"] / 100))
            contador_de_anos += 1
print(f"Vai demorar {contador_de_anos} anos")