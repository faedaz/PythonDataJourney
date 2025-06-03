import csv

#caminho para o arquivo
caminho_do_arquivo: str = "aula04/exemplo01.csv"

#armazenar os dados
arquivo_csv: list = []

#abrir o arquivo
with open(file=caminho_do_arquivo, mode="r", encoding='utf-8') as arquivo:
    #ler o arquivo
    leitor_csv=csv.DictReader(arquivo)
    #para cada linha do leitor csv vou adicionar ele no csv
    for linha in leitor_csv:
            arquivo_csv.append(linha)

#exibir
print(arquivo_csv)