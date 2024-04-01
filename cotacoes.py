import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configurações para o navegador Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument('--headless')  # Executar em modo headless (sem abrir a janela do navegador)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Inicializa o driver do navegador Chrome com as opções configuradas
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

