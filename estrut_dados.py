from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

browser = webdriver.Chrome()
url = 'https://www.noticiasagricolas.com.br/cotacoes/frutas'
browser.get(url)

newArr = [1,3,4,5,7,8,9,11,12,13,14]
text_list_preco = []
for x in newArr:
    frutas_nomes = browser.find_elements(By.CSS_SELECTOR, f'#content div.middle div.tables div:nth-child({x}) div.info h2 a')
    text_list_preco.append([texto.text for texto in frutas_nomes ])

print(text_list_preco)

df = pd.DataFrame({'Frutas': [preco for sublist in text_list_preco for preco in sublist]})

resumo = 'list_nomes.csv'
df.to_csv(resumo, index=False)

print(text_list_preco)


