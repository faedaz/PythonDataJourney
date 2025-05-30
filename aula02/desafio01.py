#Exercício 21: Conversor de Temperatura
#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura #em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado #em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    temperatura = float(input("Digite a temperatura em Celsius: "))
    conversor = (temperatura * 9/5) + 32
    print(f"A temperatura em fahrenheit é: {conversor:.2f} ")
except ValueError:
    print("Erro!\nDigite um valor válido!")