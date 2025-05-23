#Você recebe um dicionário com o estoque de produtos. Peça ao usuário o nome de um produto e a quantidade desejada. Verifique se há estoque suficiente.
#estoque = {'banana': 5, 'maçã': 10, 'laranja': 3}

estoque = {'banana': 5, 'maca': 10, 'laranja': 3}
produto = input("Digite o produto desejado (banana, maca ou laranja): ").lower()
quantidade = int(input("Digite a quantidade que deseja: "))

if produto in estoque and estoque[produto] >= quantidade:
    print("Pedido aprovado")
elif produto in estoque:
    print("Quantidade insuficiente!")
else:
    print("Produto não encontrado!")