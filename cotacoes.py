import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Config para nao abrir navegador
chrome_options = Options()
chrome_options.add_argument('--headless')  # Executar em modo headless (sem abrir a janela do navegador)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=chrome_options)

# browser = webdriver.Chrome()
url = 'https://www.noticiasagricolas.com.br/cotacoes/frutas'
browser.get(url)


txt_lista_nomes = []
txt_lista_precos = []
fruta = []

def search_bot(tam:int,id:int):
    for i in range(1,tam):
        pracas_nomes = browser.find_elements(By.CSS_SELECTOR, f'table#\\"anchor\\"{id}.cot-fisicas tbody tr:nth-child({i}) td:nth-child(1)')
        precos_produto = browser.find_elements(By.CSS_SELECTOR, f'table#\\"anchor\\"{id}.cot-fisicas tbody tr:nth-child({i}) td:nth-child(2)') 
        txt_lista_nomes.append([elemento.text for elemento in pracas_nomes])
        txt_lista_precos.append([elemento.text for elemento in precos_produto])
    return txt_lista_nomes, txt_lista_precos

# abacate = search_bot(10, 189)
# abacaxi = search_bot(7, 190)
# mamao = search_bot(10 ,191)
# maracuja = search_bot(10, 192)
# pera = search_bot(10, 193)
# tangerina = search_bot(10, 195)
# uva = search_bot(10, 194)
# melancia = search_bot(13, 89)
# banana_nanica_prata = search_bot(10, 68)
# limao_tahiti = search_bot(12, 72)
# maca_fuji = search_bot(4, 73)
# maca_gala = search_bot(4, 74)

pera_praca, pera_valor = search_bot(10, 193)
print(pera_praca)
print(pera_valor)



df = pd.DataFrame({
                'Pera Praça': [pera for sublist in pera_praca for pera in sublist],
                'Pera Preço': [pera_valor for sublist in pera_valor for pera_valor in sublist]
                })

# Salvar o DataFrame como um arquivo CSV
resumo = 'dados_frutas.csv'
df.to_csv(resumo, index=False)

