import csv

#caminho para o arquivo
caminho_arquivo: str = "aula04/exemplo01.csv"

#armazenar os dados
arquivo_csv: list = []

#abrir o arquivo
with open(file=caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
    #ler o arquivo - o dict ja pula o cabecalho
    leitor_csv = csv.DictReader(arquivo)    
    
    #iterar minha lista com os dados la do csv
    for linha in leitor_csv:
        arquivo_csv.append(linha)
        
    soma_idades: float = 0
    numero_pessoas: float = 0
    
    #acessando as variaveis e inicializando variaveis para calculo        
    for contador in arquivo_csv:
        idade_str = contador['Idade'] #como estou usando a funcao DictReader, nao preciso referenciar por numero, posso ja usar o nome do cabecalho porque a funcao le a primeira linha
        idade_float =  float(idade_str)
        soma_idades: float = soma_idades + idade_float
        numero_pessoas: float = numero_pessoas + 1
        
#Agora, depois de armazenar os numeros, faco o calculo
if numero_pessoas > 0:
    media_idades: float = float(soma_idades) / float(numero_pessoas)
    print(f"A soma das idades ({soma_idades:.0f} dividido pelo numero de pessoas ({numero_pessoas}) sera de: {media_idades:.2f}))")
else:
    print("Nenhuma pessoa encontrada!") 
        