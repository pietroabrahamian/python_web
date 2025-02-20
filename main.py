from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pyautogui
import time

# Caminho para o WebDriver
service_home= Service(r"C:\Users\Intel\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_home)
# service = Service(r"C:\Users\pietro.abrahamian\Downloads\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# URL do site
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")


wait = WebDriverWait(driver, 10) #salva na variavel WAIT a ação de esperar 10s
botao_login = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-standard call-to-action']"))) #indica que tem q usar o tempo de espera até o elemento aparecer na tela, ai sim localiar ele 
botao_login.click() # clica no botao que foi armazena na variavel acima

email = wait.until(EC.visibility_of_element_located((By.ID, "email"))) 
email.send_keys("pietroabrahamian2021@gmail.com")
# email.send_keys("pietroabrahamian2018@gmail.com")
email.send_keys(Keys.RETURN)

senha = wait.until(EC.visibility_of_element_located((By.ID, "password")))
senha.send_keys("2007Pietr@")
senha.send_keys(Keys.RETURN)

try:
    seguranca = driver.find_element(By.ID, "secureBtn")
    seguranca.click()
except Exception as e:
    codigo = driver.find_element(By.ID, "btnSendCode")
    codigo.click()

input("Faça o que precisa agora e dps pressione enter para voltar a funcionar")

dme = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-tile-content-graphic-info")))
dme.click()

dme_melhoria = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Upgrades']")))
dme_melhoria.click()

dme_bronze_diaria = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Bronze Upgrade']")))
dme_bronze_diaria.click()


def montagem():
    x = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "flat ut-search-filter-control--row-button")))
    x.click() 
    qualidade = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-search-filter-control--row")))
    qualidade.click() 
    quality_bronze = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Bronze']")))
    quality_bronze.click()
    pesquisa = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Search']")))
    pesquisa.click()
    # template_SBC = wait.until(EC.visibility_of_element_located((By.ID, "edit-template")))
    # template_SBC.click()
    # template_add = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Add']")))
    # template_add.click()
    # untradeables_only = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Untradeables Only']")))
    # untradeables_only.click()
    # sbc_storage = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='SBC Storage']")))
    # sbc_storage.click()
    # position_players = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Ignore Players Positions']")))
    # position_players.click()
    # quality = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Quality']")))
    # quality.click()
    # quality_bronze = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Bronze']")))
    # quality_bronze.click()
    # template_save = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Save']")))
    # template_save.click()
    submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
    submit.click()


condicao = True
if condicao:
    montagem()

# pyautogui.press('t')
# submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Submit']")))
# submit.click()

# def montagem_automatica():
#     dme_bronze_diariaV2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Daily Bronze Upgrade']")))
#     dme_bronze_diariaV2.click()
#     pyautogui.press('t')

# montagem_automatica()









time.sleep(3600)

