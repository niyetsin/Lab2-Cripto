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

mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")

def random_name():
	letras = string.ascii_lowercase
	name = ( ''.join(random.choice(letras) for i in range(6)))	
	return name

def random_pass():
	letras = string.ascii_lowercase
	password = ( ''.join(random.choice(letras) for i in range(6)))	
	return password

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
driver.switch_to.default_content()
driver.maximize_window()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')

nombre = random_name()
passes = random_pass()
print('Nombre: '+nombre)
print('Password: '+passes)
print('Email: '+mail.json()[0])

#-------------------------------------REGISTRO--------------------------------------------------------------

driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/user/register")
time.sleep(3)

time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "givenName")))
barra_usuario.send_keys(nombre)

time.sleep(1)
barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "affiliation")))
barra_afilation.send_keys(nombre)

time.sleep(1)
select_element = driver.find_element(By.ID,'country')
select_object = Select(select_element)
select_object.select_by_value('CL')

time.sleep(1)
barra_mail = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "email")))
barra_mail.send_keys(mail.json()[0])

time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "username")))
barra_usuario.send_keys(nombre)

time.sleep(1)
barra_clave = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_clave.send_keys(passes)

time.sleep(1)
barra_clave2 = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "password2")))
barra_clave2.send_keys(passes)

time.sleep(1)
driver.find_element(By.NAME, "privacyConsent").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "submit").click()


time.sleep(1)
driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/login/signOut")

time.sleep(4)
#-------------------------------------RECUPERAR CONTRASEÑA---------------------------------------------------------

driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/login/lostPassword")
time.sleep(3)


barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "email")))
barra_usuario.send_keys(mail.json()[0])


time.sleep(1)
driver.find_element(By.CLASS_NAME, "submit").click()
time.sleep(5)

#-------------------------------CHEQUEO MAIL Y CAMBIO DE CONTRASEÑA-----------------------------------------
#LEER LOS MAILS BUSCANDO EL QUE PERMITE CONFIRMAR EL RESTABLECIMIENTO DE CONTRASEÑA
contenido = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+mail.json()[0].split("@")[0]+"&domain="+mail.json()[0].split("@")[1])

for i in contenido.json():
	if i["subject"] == "[FE] Confirmación del restablecimiento de la contraseña":
		ide = i["id"]

mail_confirmacion = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login="+mail.json()[0].split("@")[0]+"&domain="+mail.json()[0].split("@")[1]+"&id="+str(ide))

link = mail_confirmacion.json()["textBody"].replace('\n', "").replace('\r', "").split(" ")[-5].split("contraseña:")[1][:-9]
confirmar = requests.get(link)
time.sleep(5)
contenido_clave = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+mail.json()[0].split("@")[0]+"&domain="+mail.json()[0].split("@")[1])
for i in contenido_clave.json():
	if i["subject"] == "[FE] Restablecer contraseña":
		ide2 = i["id"]
mail_con_clave = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login="+mail.json()[0].split("@")[0]+"&domain="+mail.json()[0].split("@")[1]+"&id="+str(ide2))
info_clave = mail_con_clave.json()["textBody"].replace('\n', "").replace('\r', "").split(" ")
usuario_cambio = info_clave[-8].split("Su")[0]
clave_cambio = info_clave[-5].split("Alejandro")[0]

clave = random_pass()
print('Clave nueva: '+clave)
print('usuario_cambio: '+usuario_cambio)
time.sleep(3)
driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/index")
time.sleep(3)

print("LOGEANDO PARA RECUPERAR CLAVE")
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "username")))
barra_usuario.send_keys(usuario_cambio)


time.sleep(1)
barra_clave = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_clave.send_keys(clave_cambio)

time.sleep(1)
driver.find_element(By.CLASS_NAME, "submit").click()

print("CAMBIANDO CLAVE")
time.sleep(5)
contra_actual = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "oldPassword")))
contra_actual.send_keys(clave_cambio)

time.sleep(1)
barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_afilation.send_keys(clave)

time.sleep(1)
barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password2")))
barra_afilation.send_keys(clave)

time.sleep(1)
driver.find_element(By.NAME, "submitFormButton").click()

time.sleep(10)


#-----------------------------------------LOGIN-------------------------------------------------------------
print("LOGOUT")
time.sleep(1)
driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/login/signOut")
time.sleep(4)

print("LOGEANDO")
driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/index")
time.sleep(3)


barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "username")))
barra_usuario.send_keys(nombre)


time.sleep(1)
barra_clave = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_clave.send_keys(clave)

time.sleep(1)
driver.find_element(By.CLASS_NAME, "submit").click()

#--------------------------------------CAMBIAR CONTRASEÑA---------------------------------------------------
print("CAMBIANDO CONTRASEÑA")
time.sleep(1)
driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/user/profile")

clave_nueva = random_pass()
print("clave nueva: "+clave_nueva)

time.sleep(1)
driver.find_element(By.NAME, "changePassword").click()
time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "oldPassword")))
barra_usuario.send_keys(clave)
time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "password")))
barra_usuario.send_keys(clave_nueva)
time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "password2")))
barra_usuario.send_keys(clave_nueva)

time.sleep(10)

print("LOGOUT")
time.sleep(1)
driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/login/signOut")
time.sleep(4)

driver.close()