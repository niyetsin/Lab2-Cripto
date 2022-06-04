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

'''
["9ktb1un8n@esiix.com"]
'''


mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
print(mail.json()[0])

def random_name():
	letras = string.ascii_lowercase
	name = ( ''.join(random.choice(letras) for i in range(6)))	
	return name

def random_pass():
	letras = string.ascii_lowercase
	password = ( ''.join(random.choice(letras) for i in range(9)))	
	return password

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
driver.switch_to.default_content()
driver.maximize_window()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')


driver.get("https://forums.overclockers.co.uk")
time.sleep(3)
boton_registro = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME, "p-navgroup-link--register"))).click()


time.sleep(15)
nombre_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "e7352f1529a19cad9de95a9eb1bcc37deaa5f023")))
nombre_usuario.send_keys(random_name())

time.sleep(1)
correo = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "d92b879743a5101b26217c6598c24c30e20f4620")))
correo.send_keys(mail.json()[0])

time.sleep(1)
contra = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME, "input--passwordHideShow")))
contra.send_keys(random_pass())


time.sleep(1)
select_element = driver.find_element(By.NAME,'dob_month')
select_object = Select(select_element)
select_object.select_by_value('1')

time.sleep(1)
barra_mail = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "location")))
barra_mail.send_keys(random_name())

time.sleep(15)
privacidad = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "accept"))).click()

time.sleep(1)
driver.find_element(By.id, "js-signUpButton").click()


contenido = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+mail.json().split("@")[0]+"&domain="+mail.json().split("@")[1])
print(contenido.json())
for i in contenido.json():
	if i["subject"] == "Overclockers UK Forums - Account confirmation required":
		ide = i["id"]

mail_confirmacion = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login="+mail.json().split("@")[0]+"&domain="+mail.json().split("@")[1]+"&id="+str(ide))
link = mail_confirmacion.json()["textBody"].replace('\n', "").replace('\r', "").split(" ")[-5]
confirmar = requests.get(link)
contenido_clave = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login=z7zjfrpj&domain=bheps.com")
for i in contenido.json():
	if i["subject"] == "[FE] Restablecer contraseña":
		ide2 = i["id"]
mail_con_clave = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login=z7zjfrpj&domain=bheps.com&id="+str(ide2))
clave = mail_con_clave.json()["textBody"].replace('\n', "").replace('\r', "").split(" ")
link = clave[-8].split("Su")[0]

time.sleep(4)
driver.close()