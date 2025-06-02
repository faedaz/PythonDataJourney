# 1, 2 e 3: Criando a lista agenda com dicionários de contatos
agenda = [
    {
        "nome": "Carlos Silva",
        "telefone": "11999998888",
        "email": "carlos.silva@email.com"
    },
    {
        "nome": "Mariana Alves",
        "telefone": "21988887777",
        "email": "mariana.alves@email.com"
    },
    {
        "nome": "Pedro Costa",
        "telefone": "31977776666",
        "email": "pedro.costa@email.com"
    },
    { # Adicionando um quarto contato para variar
        "nome": "Ana Beatriz",
        "telefone": "41966665555",
        "email": "ana.beatriz@email.com"
    }
]

# 4. Escrevendo o código para imprimir as informações solicitadas:

# Imprimir o nome e o email do segundo contato da agenda
# Lembre-se que as listas são indexadas a partir de 0, então o segundo contato está no índice 1.
print("--- Detalhes do Segundo Contato ---")
if len(agenda) > 1:  # Verifica se existe pelo menos um segundo contato
    segundo_contato = agenda[1]
    print(f"Nome: {segundo_contato['nome']}")
    print(f"Email: {segundo_contato['email']}")
else:
    print("Não há segundo contato na agenda.")

print("\n--- Nomes de Todos os Contatos na Agenda ---")
# Imprimir todos os nomes dos contatos na agenda
if agenda: # Verifica se a agenda não está vazia
    for contato in agenda:
        print(contato["nome"])
else:
    print("A agenda está vazia.")