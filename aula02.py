# Passo 1 - Importar a base de dados
from pickle import TRUE
import pandas as pd;
tabela = pd.read_csv('telecom_users.csv')

# Informação que não te ajuda, te atrapalha!

# Passo 2 - Visualizar a base de dados 
 # Entender as informações que você tem disponível
 # Descobrir os erros da base de dados
tabela = tabela.drop("Unnamed: 0", axis= 1) # O método drop trabalha com o nome da linha/coluna e com o eixo (0 = linha e 1 = coluna). É utilizado para excluir alguma linha ou coluna que não nos ajudam.
print(tabela)

# Passo 3 - Tratamento dos dados (resolver os problemas/erros)
# Informações do tipo correto - Ajustar o total gasto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors= "coerce")
# O método dropna serve para excluir informações vazias
# Colunas completamente vazias - axis -> 1
tabela = tabela.dropna(how= "all", axis= 1) # how = all exclui todas as colunas completamente vazias
# Linhas completamente vazias - axis -> 0
tabela = tabela.dropna(how= "any", axis= 0) # how = any exclui linhas em que alguma informação está vazia
print(tabela.info())

# Passo 4 - Análise inicial dos dados
print(tabela["Churn"].value_counts()) # Verificar quantos clientes cancelaram ou não
print(tabela["Churn"].value_counts(normalize= True).map("{:.1%}".format)) # normalize = True mostra os valores para conversão de percentual

# Passo 5 - Descobrir os motivos do cancelamento
