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
mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
mail_split = mail.json()[0].split("@")
contenido = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+mail_split[0]+"&domain="+mail_split[1])
'''
def random_pass():
	letras = string.ascii_lowercase
	password = ( ''.join(random.choice(letras) for i in range(6)))	
	return password

contenido = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login=z7zjfrpj&domain=bheps.com")
print(contenido.json())
for i in contenido.json():
	if i["subject"] == "[FE] Confirmación del restablecimiento de la contraseña":
		ide = i["id"]

mail_confirmacion = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login=z7zjfrpj&domain=bheps.com&id="+str(ide))
link = mail_confirmacion.json()["textBody"].replace('\n', "").replace('\r', "").split(" ")[-5].split("contraseña:")[1][:-9]
confirmar = requests.get(link)
contenido_clave = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login=z7zjfrpj&domain=bheps.com")
for i in contenido.json():
	if i["subject"] == "[FE] Restablecer contraseña":
		ide2 = i["id"]
mail_con_clave = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login=z7zjfrpj&domain=bheps.com&id="+str(ide2))
clave = mail_con_clave.json()["textBody"].replace('\n', "").replace('\r', "").split(" ")
usuario_cambio = clave[-8].split("Su")[0]
clave_cambio = clave[-5].split("Alejandro")[0]


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
driver.switch_to.default_content()
driver.maximize_window()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
clave_nueva = random_pass()
print(clave_nueva)

driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/login/changePassword/"+usuario_cambio)
time.sleep(3)


time.sleep(1)
contra_actual = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "oldPassword")))
contra_actual.send_keys(clave_cambio)

time.sleep(1)
barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_afilation.send_keys(clave_nueva)

time.sleep(1)
barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password2")))
barra_afilation.send_keys(clave_nueva)

time.sleep(1)
driver.find_element(By.NAME, "submitFormButton").click()

time.sleep(4)
driver.close()