#funcao para ordernar

lista_de_numeros: list = [5, 1, 4, 2, 8]
print(f"lista: {lista_de_numeros}")

n: int = len(lista_de_numeros)
print(f"numero de elementos dentro da lista: {n}")

# Laço Externo: Controla o número de passagens
for i in range(n -1):
    print(f"----Inicio da passagem: {i + 1}----")
    houve_troca_nesta_passagem: bool = False
    # Laço Interno: Percorre a parte da lista que ainda não está ordenada, comparando pares de elementos vizinhos.
    for j in range(n - 1 - i):
        print(f"Comparando índice {j} (valor {lista_de_numeros[j]}) com índice {j+1} (valor {lista_de_numeros[j+1]})")
        # Condição: Se o elemento da esquerda for maior que o elemento da direita
        if lista_de_numeros[j] > lista_de_numeros[j+1]:
            print(f"   TROCA! {lista_de_numeros[j]} é maior que {lista_de_numeros[j+1]}.")
            # Realiza a troca dos elementos de lugar
            lista_de_numeros[j], lista_de_numeros[j+1] = lista_de_numeros[j+1], lista_de_numeros[j]
            houve_troca_nesta_passagem = True  # Marca que uma troca ocorreu nesta passagem
        else:
            print(f"   SEM TROCA. {lista_de_numeros[j]} não é maior que {lista_de_numeros[j+1]}.")

        print(f"   Estado atual da lista: {lista_de_numeros}")

    print(f"--- Fim da Passagem {i + 1} ---")
    print(f"Lista após Passagem {i + 1}: {lista_de_numeros}\n")

    # Otimização: Se nenhuma troca foi feita durante uma passagem completa,
    # significa que a lista já está ordenada. Podemos parar.
    if not houve_troca_nesta_passagem:
        print("Nenhuma troca foi realizada nesta passagem, então a lista já está ordenada.")
        break  # Interrompe o laço externo (o laço de 'i')

print(f"Resultado Final (lista ordenada): {lista_de_numeros}")