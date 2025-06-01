#crie um dicionario para armazenar informacoes de um livro, com titulo, autor e ano de publicacoa.

from typing import Dict, Any

livro1: Dict[str, Any] = {
    "Titulo": "Senhor dos Aneis - Socieidade do Anel",
    "Autor": "J.R.R. Tolkien",
    "Ano": 1994
}

livro2: Dict[str, Any] = {
    "Titulo": "Senhor dos Aneis - Duas Torres",
    "Autor": "J.R.R. Tolkien",
    "Ano": 1994
}

lista_de_livros = []

lista_de_livros.append(livro1)
lista_de_livros.append(livro2)

biblioteca: dict = {
        "livro1": {
        "Titulo": "Senhor dos Aneis - Socieidade do Anel",
        "Autor": "J.R.R. Tolkien",
        "Ano": 1994
    },

    "livro2": {
        "Titulo": "Senhor dos Aneis - Duas Torres",
        "Autor": "J.R.R. Tolkien",
        "Ano": 1994
    }
}
print(f"Biblioteca: \n {biblioteca}")