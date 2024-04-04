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


# txt_lista_nomes = []
# txt_lista_precos = []

def search_bot(tam:int,id:int):
    txt_lista_nomes = []
    txt_lista_precos = []
    for i in range(1,tam):
        pracas_nomes = browser.find_elements(By.CSS_SELECTOR, f'table#\\"anchor\\"{id}.cot-fisicas tbody tr:nth-child({i}) td:nth-child(1)')
        precos_produto = browser.find_elements(By.CSS_SELECTOR, f'table#\\"anchor\\"{id}.cot-fisicas tbody tr:nth-child({i}) td:nth-child(2)') 
        txt_lista_nomes.append([elemento.text for elemento in pracas_nomes])
        txt_lista_precos.append([elemento.text for elemento in precos_produto])
    return txt_lista_nomes, txt_lista_precos

abacate_local, abacate_preco = search_bot(10, 189)
abacaxi_local, abacaxi_preco = search_bot(7, 190)
mamao_local, mamao_preco = search_bot(10 ,191)
maracuja_local, maracuja_preco = search_bot(10, 192)
pera_local, pera_preco = search_bot(10, 193)
tangerina_local, tangerina_preco = search_bot(10, 195)
uva_local, uva_preco = search_bot(10, 194)
melancia_local, melancia_preco = search_bot(13, 89)
banana_nanica_prata_local, banana_nanica_prata_preco = search_bot(10, 68)
limao_tahiti_local, limao_tahiti_preco = search_bot(12, 72)
maca_fuji_local, maca_fuji_preco = search_bot(4, 73)
maca_gala_local, maca_gala_preco = search_bot(4, 74)


df = pd.DataFrame({
                'Pera Praça': abacate_local,
                'Pera Preço': abacate_preco
                })

# Salvar o DataFrame como um arquivo CSV
resumo = 'dados_frutas.csv'
df.to_csv(resumo, index=False)

