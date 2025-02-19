from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Caminho para o WebDriver
service = Service(r"C:\Users\pietro.abrahamian\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL do site
driver.get("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/")


wait = WebDriverWait(driver, 10) #salva na variavel WAIT a ação de esperar 10s
botao_login = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-standard call-to-action']"))) #indica que tem q usar o tempo de espera até o elemento aparecer na tela, ai sim localiar ele 
botao_login.click()

email = wait.until(EC.visibility_of_element_located((By.ID, "email"))) 
email.send_keys("pietroabrahamian2018@gmail.com")
email.send_keys(Keys.RETURN)

senha = wait.until(EC.visibility_of_element_located((By.ID, "password")))
senha.send_keys("2007Pietr@")
senha.send_keys(Keys.RETURN)

codigo = driver.find_element(By.ID, "btnSendCode")
codigo.click()

input("Faça o que precisa agora e dps pressione enter para voltar a funcionar")

dme = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ut-tile-content-graphic-info")))
dme.click()

dme_melhoria = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Upgrades']")))
dme_melhoria.click()





time.sleep(3600)

