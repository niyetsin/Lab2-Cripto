from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #se hace envios POST
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import string
import random
import requests


mail = "9ktb1un8n@esiix.com"

contenido = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+mail.split("@")[0]+"&domain="+mail.split("@")[1])
print(contenido.json())
'''
for i in contenido.json():
	if i["subject"] == "Overclockers UK Forums - Account confirmation required":
		ide = i["id"]
'''
mail_confirmacion = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login="+mail.split("@")[0]+"&domain="+mail.split("@")[1]+"&id="+str(ide))
print(mail_confirmacion.json()["textBody"])
'''
link = mail_confirmacion.json()["textBody"].replace('\n', "").replace('\r', "").split(" ")[-5]
confirmar = requests.get(link)
contenido_clave = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login=z7zjfrpj&domain=bheps.com")
for i in contenido.json():
	if i["subject"] == "[FE] Restablecer contraseña":
		ide2 = i["id"]
mail_con_clave = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login=z7zjfrpj&domain=bheps.com&id="+str(ide2))
clave = mail_con_clave.json()["textBody"].replace('\n', "").replace('\r', "").split(" ")
link = clave[-8].split("Su")[0]

'''