from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
# import pyautogui
# import time

import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk



def criar_skype():
    # Caminho para o WebDriver
    service_home= Service(r"C:\Users\Intel\Downloads\chromedriver-win64\chromedriver.exe")
    # service = Service(r"C:\Users\pietro.abrahamian\Downloads\chromedriver-win64\chromedriver.exe")
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome(service=service_home)

    # URL do site
    driver.get(f"https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=171&ct=1739990668&rver=7.5.2156.0&wp=MBI_SSL&wreply=https%3a%2f%2flw.skype.com%2flogin%2foauth%2fproxy%3fclient_id%3d578134%26redirect_uri%3dhttps%253A%252F%252Fweb.skype.com%26source%3dscomnav%26form%3dmicrosoft_registration%26fl%3dphone2&lc=1033&id=293290&mkt=pt-BR&psi=skype&lw=1&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&client_flight=ReservedFlight33%2CReservedFligh&fl=phone2&lic=1&uaid=95e019bb4f1342199eddb75c83401474")

    wait = WebDriverWait(driver, 10) #tempo de espera: 10s

    email= entry_email.get() # puxa o email inserido na janela
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "usernameInput")))
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN )

    senha = entry_senha.get()
    senha_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
    senha_input.send_keys(senha)
    senha_input.send_keys(Keys.RETURN)


    #separa as informações do email para retirar o nome
    nome_usuario = email.split('@')[0] #separa no @
    nome = nome_usuario.split('.')[0]
    sobrenome = nome_usuario.split('.')[1]
    nome = nome.capitalize() #primeira letra amiusucla
    sobrenome = sobrenome.capitalize() 

    nome_input = wait.until(EC.visibility_of_element_located((By.ID, "firstNameInput")))
    nome_input.send_keys(nome)
    nome_input.send_keys(Keys.RETURN)
    sobrenome_input = wait.until(EC.visibility_of_element_located((By.ID, "lastNameInput")))
    sobrenome_input.send_keys(sobrenome)
    sobrenome_input.send_keys(Keys.RETURN)

    # selecionando a data e inserindo o ano
    dia_input = wait.until(EC.visibility_of_element_located((By.ID, 'BirthDay')))
    dia_input.click()
    dia = wait.until(EC.visibility_of_element_located((By.XPATH, '//option[text()="1"]')))
    dia.click()
    mes_input = wait.until(EC.visibility_of_element_located((By.ID, 'BirthMonth')))
    mes_input.click()
    mes = wait.until(EC.visibility_of_element_located((By.XPATH, '//option[text()="janeiro"]')))
    mes.click()
    ano_input = wait.until(EC.visibility_of_element_located((By.ID, 'BirthYear')))
    ano_input.send_keys("2000")
    ano_input.click()
    ano_input.send_keys(Keys.RETURN)


    #abre um link em uma nova aba
    driver.execute_script("window.open('https://webmail.mandic.com.br/', '_blank');") 

    #guarda uma lista de todas as abas dentro de uma variavel
    abas = driver.window_handles
    driver.switch_to.window(abas[1]) #vai para a segunda aba, logo, o link q foi aberto

    #  entrar no webmail mandic
    email_madic_input = wait.until(EC.visibility_of_element_located((By.ID, "login_username")))
    email_madic_input.click()
    email_madic_input.send_keys(email)

    senha_mandic_input = wait.until(EC.visibility_of_element_located((By.ID, "secretkey")))
    senha_mandic_input.send_keys(senha)
    senha_mandic_input.send_keys(Keys.RETURN)

    caixa_entrada = wait.until(EC.visibility_of_element_located((By.ID, "extdd-1")))
    caixa_entrada.click()
    email_outlook = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "x-grid3-row x-grid3-row-first")))
    email_outlook.click()






janela = tk.Tk()
janela.title("Gerador de Skype")
janela.geometry("500x200")

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

frame = ctk.CTkFrame(janela, width=1000, height=250, corner_radius=10)
frame.pack(padx=20, pady=20, fill="both", expand=True)

label_email = ctk.CTkLabel(frame, text="Insira o Email do colaborador:", font=("Arial", 16))
label_email.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_email = ctk.CTkEntry(frame, width=200, font=("Arial", 12))
entry_email.grid(row=0, column=1, padx=10, pady=10)
entry_email.focus_set()

label_senha = ctk.CTkLabel(frame, text="Senha para usuário:", font=("Arial", 16))
label_senha.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_senha = ctk.CTkEntry(frame, width=200, font=("Arial", 12))
entry_senha.grid(row=1, column=1, padx=10, pady=10)


botao = ctk.CTkButton(frame, text="Criar", font=("Arial", 16), command=criar_skype)
botao.grid(row=2, column=0, columnspan=2, pady=20)

janela.bind("<Return>", criar_skype)

janela.mainloop()