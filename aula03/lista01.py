##Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    try:
        nota = int(input("De uma nota de zero a 10: "))
        if 0 <= nota <= 10:
            break
        else:
            print("A nota deve ser entre 0 e 10")
    except ValueError:
        print("Valor invalido!")