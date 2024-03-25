import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import indices

browser = webdriver.Chrome()
url = 'https://www.noticiasagricolas.com.br/cotacoes/frutas'
browser.get(url)

text_list_preco = []
text_list_praca = []
text_list_indice = []

for i in range(13):
    lista_preco = browser.find_elements(By.CSS_SELECTOR, f'.tables .cotacao .table-content .cot-fisicas tbody tr:nth-child({i}) td:nth-child(2)')
    lista_pracas = browser.find_elements(By.CSS_SELECTOR, f'.tables .cotacao .table-content .cot-fisicas tbody tr:nth-child({i}) td:nth-child(1)')
    text_list_preco.append([texto.text for texto in lista_preco])
    text_list_praca.append([texto.text for texto in lista_pracas])



# print(text_list_preco)
# print(text_list_praca)


df = pd.DataFrame({
                'Local': [local for sublist in text_list_praca for local in sublist],
                'Preço': [preco for sublist in text_list_preco for preco in sublist]
                })

# Salvar o DataFrame como um arquivo CSV
resumo = 'dados_frutas.csv'
df.to_csv(resumo, index=False)

# maracujas = []
# for maracuja in text_list_praca:
#     try:
#         maracujas.append(maracuja[indices.maracuja_indice])
#     except:
#         pass
# print(maracujas)
