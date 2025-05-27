#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

numero = 1
numero2 = 1

while numero < 21:
    print(f"{numero}")
    numero += 1
    if numero == 21:
        while numero2 < 21:
            print(f"{numero2}", end=' ')
            numero2 += 1
