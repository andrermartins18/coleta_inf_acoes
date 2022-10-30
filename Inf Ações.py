import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


grupo_acoes = []
#fazendo a lista de ações que queremos

acoes = input('Qual o nome da ação que deseja pesquisar?')
grupo_acoes.append(acoes)
pergunta = input('Quer adicionar mais alguma ação? (S/N)').upper()
while pergunta != 'N':
    acoes = input('Qual o nome da ação que deseja pesquisar?')
    grupo_acoes.append(acoes)
    pergunta = input('Quer adicionar mais alguma ação? (S/N)').upper()

print('Ações cadastradas foram essas {}, aguarde!'.format(grupo_acoes))

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://fundamentus.com.br/')

nome_acao = []
valor_acao = []
var_dia = []
data_acao = []
valor_min = []
valor_max = []
ult_30_dias = []
empresa = []

for i in grupo_acoes:
    
    #Buscando e acessando a ação!
    busca_acao = navegador.find_element(By.ID, 'completar')
    busca_acao.send_keys(i)
    navegador.find_element(By.CLASS_NAME, 'botao').click()

    #buscar dados da ação
    nome_acao.append(navegador.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[2]').text)
    valor_acao.append(navegador.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[4]').text)
    var_dia.append(navegador.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[2]').text)
    data_acao.append(navegador.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/table[1]/tbody/tr[2]/td[4]').text)
    valor_min.append(navegador.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/table[1]/tbody/tr[3]/td[4]').text)
    valor_max.append(navegador.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[4]').text)
    ult_30_dias.append(navegador.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/table[3]/tbody/tr[4]/td[2]').text)
    empresa.append(navegador.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/table[1]/tbody/tr[3]/td[2]').text)


df = pd.DataFrame(list(zip(
    data_acao, nome_acao, empresa, valor_acao, var_dia, valor_max, valor_min, ult_30_dias)),
                  columns = ['Data', 'Papel', 'Empresa', 'Valor da Ação', 'Variação do dia', 'Mín 52 sem', 'Max 52 sem', '30 dias'])

print(df)

df.to_excel('Acoes.xlsx')
