import os
import glob


arquivo = 'dados_frutas.csv'
arquivo = open(arquivo, 'r', newline='')


with open('dados_frutas.csv', encoding='utf-8') as arquivo:
    dados = arquivo.readlines()



# linhas = []
# for i in dados:
#     linhas.append(i.replace(",",".", 1).replace('\n', '').split())

# print(linhas)

# for x in linhas:
#     print(x)

abacate = [2,14,26,38,48,58,68,77,86]
new_abacate = []

for indice, linha in enumerate(dados, start=1):
    # Verificando se o índice da linha está na lista de linhas para selecionar
    if indice in abacate:
        # Adicionando a linha selecionada à lista
        new_abacate.append(linha)

# print(abacate)
for x in new_abacate:
    print(x)