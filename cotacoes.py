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

for i in range(indices.maca_fuji + 1):
    lista_preco = browser.find_elements(By.CSS_SELECTOR, f'.tables .cotacao .table-content .cot-fisicas tbody tr:nth-child({i}) td:nth-child(2)')
    lista_pracas = browser.find_elements(By.CSS_SELECTOR, f'.tables .cotacao .table-content .cot-fisicas tbody tr:nth-child({i}) td:nth-child(1)')
    text_list_preco.append([texto.text for texto in lista_preco])
    text_list_praca.append([texto.text for texto in lista_pracas])

# print(text_list_preco)
# print(text_list_praca)

df = pd.DataFrame({'Preço': [preco for sublist in text_list_preco for preco in sublist], 'Local': [local for sublist in text_list_praca for local in sublist]})

# Salvar o DataFrame como um arquivo CSV
resumo = 'dados_frutas.csv'
df.to_csv(resumo, index=False)

#let test = document.querySelector(`div:nth-child(4)  div.info  h2  a`).innerText
#console.log(test)

maca_fuji = []
for x in text_list_praca:
    try:
        maca_fuji.append(x[indices.maca_fuji_indice])
    except:
        pass
    
print(maca_fuji)