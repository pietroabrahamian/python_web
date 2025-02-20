from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

#onde o webdriver está no meu pc
service = Service(r"C:\Users\pietro.abrahamian\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL do site
driver.get(f"https://webmail.mandic.com.br/")

wait = WebDriverWait(driver, 10) # tempo de espera padrão
#  entrar no webmail mandic
email_madic_input = wait.until(EC.visibility_of_element_located((By.ID, "login_username")))
email_madic_input.send_keys("mariana.santos@workongroup.com.br") #loga com o meu email

senha_mandic_input = wait.until(EC.visibility_of_element_located((By.ID, "secretkey")))
senha_mandic_input.send_keys("MaS@work2025")# com a minha senha
senha_mandic_input.send_keys(Keys.RETURN)#clica no ENTER

# entra na caixa de entrada e entra no primeiro email da caixa
caixa_entrada = wait.until(EC.visibility_of_element_located((By.ID, "extdd-1")))
caixa_entrada.click()
#clica no email com esse titulo
email_outlook = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Verifique seu endereço de email"]')))
#da double.click para abrir o email
acoes = ActionChains(driver)
acoes.double_click(email_outlook).perform()

#armaneza e acessa o corpo do email (texto)
corpo_email = wait.until(EC.visibility_of_element_located((By.XPATH, '//td[contains(@style, "padding:0"/span"/span/font/font')))
texto_email = corpo_email.text

print("O codigo de verificação é:", texto_email)


time.sleep(3600)

