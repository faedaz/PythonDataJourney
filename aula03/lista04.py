##Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao = {"A": 80000, "B": 200000}

crescimento_A = 0.03
crescimento_B = 0.015
contador_de_anos = 0

while populacao["A"] <= populacao["B"]:
    populacao["A"] = int(populacao["A"] * (1 + crescimento_A))
    populacao["B"] = int(populacao["B"] * (1 + crescimento_B))
    contador_de_anos = contador_de_anos + 1
print(f"Vai demorar {contador_de_anos} anos")