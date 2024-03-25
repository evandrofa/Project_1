import os
import glob


arquivo = 'dados_frutas.csv'
arquivo = open(arquivo, 'r', newline='')


with open('dados_frutas.csv', encoding='utf-8') as arquivo:
    dados = arquivo.readlines()

linhas = []
for linha in dados:
    linhas.append(linha.replace(",",".",1).replace("\n",'').split(','))

for l in linhas:
    print(l)




names =[
'abacaxi',
'mamao',
'maracuja',
'pera',
'tangerina',
'uva',
'melancia',
'banana',
'limao',
'maca_fuji',
'maca_gala'
]

indices = {
'abacate_indice': 0,
'abacaxi_indice': 1,
'mamao_indice': 2,
'maracuja_indice': 3,
'pera_indice': 4,
'tangerina_indice': 5,
'uva_indice': 6,
'melancia_indice': 7,
'banana_indice': 8,
'limao_indice': 9,
'maca_fuji_indice': 10,
'maca_gala_indice': 11
}
