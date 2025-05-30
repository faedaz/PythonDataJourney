##A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o 20 termo.

fibonacci = []
anterior = 1
atual = 1

for i in range(1, 21):
    fibonacci.append(anterior)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    
print(fibonacci)