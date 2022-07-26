from ctypes import py_object
import pyautogui;
import pyperclip;
import time;
import pandas as pd;

pyautogui.PAUSE = 1

#Passo 1 - Entrar no sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
#Aguardar o site carregar
time.sleep(5)

#Passo 2 - Navegar pelo sistema e localizar a base de dados
pyautogui.click(x=405, y=315, clicks=2)
time.sleep(1.7)

#Passo 3 - Baixar a base de dados
pyautogui.click(x=416, y=366)
time.sleep(1.7)
pyautogui.click(x=1159, y=185)
time.sleep(1.7)
pyautogui.click(x=972, y=616)

#Passo 4 - Importar a tabela
time.sleep(5)
tabela = pd.read_excel(r'C:\Users\User\Downloads\Vendas - Dez.xlsx')
print(tabela)

#Passo 5 - Soma da quantidade e do faturamento
quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()
print(quantidade)
print(faturamento)

#Passo 6 - Mandar para o email
pyautogui.hotkey("ctrl", "t") #Comando para abrir uma nova aba
pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=46, y=202)

#Destinatário do Email
pyautogui.write("mateus.rauli@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

#Assunto do Email
pyperclip.copy("Relatório De Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

#Corpo do Email
texto = f"""
Prezados, bom dia
O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos é de: {quantidade:,}

Abs
Mateus Rauli Giacoia Chioquetta
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
#Enviar o Email
time.sleep(1.5)
pyautogui.hotkey("ctrl", "enter")

# # #O método abaixo serve para mostrar em que coordenada o nosso mouse está na tela, facilitando para que possamos usar o método click()
# time.sleep(5)
# print(pyautogui.position())