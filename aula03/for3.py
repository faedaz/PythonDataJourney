#faca um programa qual leia um numero inteiro e diga se ele e ou nao um numero primo

numero_primo = int(input("Digite um valor: "))

if numero_primo <= 1:
    print("Não é primo!")
else:
    eh_primo = True
    for i in range(2, numero_primo):
        if numero_primo % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("É primo!")
    else:
        print("Não é primo!")
        