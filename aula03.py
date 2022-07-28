import imp;
from lib2to3.pgen2 import driver;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
import pandas as pd;

# Passo 1 - Pegar a cotação do Dólar
navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')
navegador.get('https://www.google.com.br/?gws_rd=ssl')
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dólar") # Pesquisando a cotação no google
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) 
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value') # Pegando a cotação

print(cotacao_dolar)

# Passo 2 - Pegar a cotação do Euro
navegador.get('https://www.google.com.br/?gws_rd=ssl')
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação euro") # Pesquisando a cotação no google
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) 
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value') # Pegando a cotação

print(cotacao_euro)

# Passo 3 - Pegar a cotação do Ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

navegador.quit()

# Passo 4 - Importar a base de dados
tabela = pd.read_excel("Produtos.xlsx")

# Passo 5 - Recalcular os valores atualizados
# Atualizar as cotações
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
# Preço de Compra = Preço Original * Cotação
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
# Preço de Venda = Preço de Compra * Margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
print(tabela)

# Passo 6 - Exportar a base de dados
tabela.to_excel("Produtos Novo.xlsx", index=False)