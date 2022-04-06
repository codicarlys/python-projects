from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import logging


# Setting log Config
logging.basicConfig(level=logging.DEBUG)

# Environment Variables
chromedriver_path=r'D:\ecarlos\softwares\chromedriver\chromedriver.exe'
path = 'D:/ecarlos/downloads/'
filename = 'Lancamento_horas_2022.xlsx'
website = 'http://discovery.leega.com.br/'
mes = 'março'
usuario = 'ecarlos'
senha = 'leega5on2#L'
feriados = ['01/03/2022','02/03/2022']

def setBrowser():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chromedriver_path,options=option)
    logging.info('Driver Selenium setado com sucesso')
    return driver

def discovery(driver,site):
    """Input: Driver: Selenium ; Site: site accessed """

    # Access site and resize browser window
    driver.get(site)
    driver.set_window_size(1024,768)
    logging.info('Homepage Access')

    # Homepage
    driver.find_element_by_name('Login').send_keys(usuario)
    driver.find_element_by_name('Password').send_keys(senha)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/input').click()
    time.sleep(2)

    # Pagina Inicial
    driver.find_element_by_xpath('//*[@id="ctl00_PainelUsuario"]/div/ul/li[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ctl00_PainelUsuario"]/div/ul/li[2]/ul/li[2]/a').click()
    logging.info('Acessado pagina Painel')
    time.sleep(2)

    # Pagina de apontamento
    driver.find_element_by_xpath('//*[@id="ctl00_MainContent_GradeAtividade_ctl02_LinkApontamento"]/i').click()
    logging.info('Acessado pagina de Apontamento')
    time.sleep(2)

def generate_dataframe(path,filename) -> pd.DataFrame :
    """Input: File path ; Filename  Output: Dataframe """
    df = pd.read_excel(f'{path}{filename}')
    header = [ value.replace(' ','_').lower() for value in df.columns.values ]
    df.columns = header
    return df

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame :
    """Input: Dataframe Output: Filter Dataframe"""
    df = df[df['mes'] == mes] # month filter
    df = df[~df['dia_semana'].isin(['sábado','domingo']) ] # Remove weekends
    df = df[(df.data > '2022-03-14')]
    
    df = df.astype('str')
    df.data = df.data.apply( lambda x: f"{x[8:10]}/{x[5:7]}/{x[0:4]}")
    df = df[~df['data'].isin(feriados) ] # Remove weekends
    return df

# Lancamento Horas
def lanca_hora(driver, dia,hr_inicio,hr_fim,esforco,observacao):
    driver.find_element_by_name('ctl00$MainContent$ControleApontamento$txtDataApontamento').send_keys(dia)
    driver.find_element_by_name('ctl00$MainContent$ControleApontamento$CaixaHoraInicial').send_keys(hr_inicio)
    driver.find_element_by_name('ctl00$MainContent$ControleApontamento$CaixaHoraFinal').send_keys(hr_fim)
    driver.find_element_by_name('ctl00$MainContent$ControleApontamento$CaixaEsforço').send_keys(esforco)
    time.sleep(6)

    driver.find_element_by_name('ctl00$MainContent$ControleApontamento$CaixaStatus').send_keys(1)
    driver.find_element_by_name('ctl00$MainContent$ControleApontamento$CaixaObservaçao').send_keys(observacao)
    driver.find_element_by_name('ctl00$MainContent$ControleApontamento$BotaoSalvar').click()
    time.sleep(6)

def main():

    # Read excel file
    df = generate_dataframe(path,filename) # lendo arquivo de horas
    df = clean_dataframe(df)
    df = df.astype('str')

    # Create driver selenium
    driver = setBrowser()

    # Acessa site discovery
    discovery(driver, website) 

    # Lancando Horas
    for _, row in df.iterrows():

        # horario manha
        print(row['data'],row['hr_inicio_m'],row['hr_fim_m'],row['esforco_m'],row['obs_m'])
        lanca_hora(driver,row['data'],row['hr_inicio_m'],row['hr_fim_m'],row['esforco_m'],row['obs_m'])
        time.sleep(2)

        # horario tarde
        print(row['data'],row['hr_inicio_t'],row['hr_fim_t'],row['esforco_t'],row['obs_t'])
        lanca_hora(driver,row['data'],row['hr_inicio_t'],row['hr_fim_t'],row['esforco_t'],row['obs_t'])
        time.sleep(2)
    
    # Fechado driver
    driver.close()

main()