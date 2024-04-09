import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import date

data_hoje = date.today()
data_formatada = data_hoje.strftime("%d/%m/%Y")

# Config para nao abrir navegador
chrome_options = Options()
chrome_options.add_argument('--headless')  # Executar em modo headless (sem abrir a janela do navegador)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=chrome_options)

# browser = webdriver.Chrome()
url = 'https://www.noticiasagricolas.com.br/cotacoes/frutas'
browser.get(url)

def search_bot(tam:int,id:int):
    txt_lista_nomes = []
    txt_lista_precos = []
    for i in range(1,tam):
        pracas_nomes = browser.find_elements(By.CSS_SELECTOR, f'table#\\"anchor\\"{id}.cot-fisicas tbody tr:nth-child({i}) td:nth-child(1)')
        precos_produto = browser.find_elements(By.CSS_SELECTOR, f'table#\\"anchor\\"{id}.cot-fisicas tbody tr:nth-child({i}) td:nth-child(2)') 
        txt_lista_nomes.extend([elemento.text for elemento in pracas_nomes])
        txt_lista_precos.extend([elemento.text for elemento in precos_produto])
    return txt_lista_nomes, txt_lista_precos

frutas = {
    'abacate': [search_bot(10, 189)],
    'abacaxi': [search_bot(7, 190)],
    'mamao': [search_bot(10 ,191)],
    'maracuja': [search_bot(10, 192)],
    'pera': [search_bot(10, 193)],
    'tangerina': [search_bot(10, 195)],
    'uva': [search_bot(10, 194)],
    'melancia': [search_bot(13, 89)],
    'banana': [search_bot(10, 68)],
    'limao_tahiti': [search_bot(12, 72)],
    'maca_fuji': [search_bot(4, 73)],
    'maca_gala': [search_bot(4, 74)]
}

for fruta, resultado in frutas.items():
    local, preco = resultado[0]  # Extrair os resultados
    df = pd.DataFrame({'Local': local, 'Preço': preco})
    # Salvar em um arquivo CSV separado
    local_salvar = os.path.join('data', fruta + '_data.csv')
    df.to_csv(local_salvar, index=False)
