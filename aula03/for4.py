import unicodedata
import re

def eh_palindromo(frase):
    # Remove acentos
    frase = ''.join(
        c for c in unicodedata.normalize('NFD', frase)
        if unicodedata.category(c) != 'Mn'
    )
    # Remove tudo que não for letra ou número
    frase = re.sub(r'[^a-zA-Z0-9]', '', frase)
    # Converte para minúsculas
    frase = frase.lower()
    
    # Verifica se é palíndromo
    return frase == frase[::-1]