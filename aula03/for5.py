#contar letras
frase = "A base do teto desaba!"
contador = 0
contadora = 0

for caractere in frase:
    if caractere.isalpha():  # verifica se é uma letra
        contador += 1
    if caractere.lower() == 'a':
        contadora += 1

print("Quantidade de letras:", contador)
print("Quantidade de letras a:", contadora)