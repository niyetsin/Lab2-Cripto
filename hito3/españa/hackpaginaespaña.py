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

def random_pass():#4 caracteres
	letras = string.ascii_lowercase
	password = ( ''.join(random.choice(letras) for i in range(4)))	
	return password

telefono = '111111111'#9 caracteres
cumple = '1969-11-11'#formato de nacimiento
direccion = '1111'#3 caracteres
ciudad = '1111'#2 caracteres
password = random_pass()#4 caracteres
postal = '01001'#5 caracteres

#NO NECESITA CONFIRMACION DE MAIL

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

driver.get("https://offspringinc.es/register")
time.sleep(8)
#Cerrar cookie
driver.find_element(By.CLASS_NAME,"close").click()
#NOMBRE
time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "firstname")))
barra_usuario.send_keys(nombre)
#APELLIDO
time.sleep(1)
barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "lastname")))
barra_afilation.send_keys(nombre)
#MAIL
time.sleep(1)
barra_mail = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "email")))
barra_mail.send_keys(mail.json()[0])
#TELEFONO
time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "telephone")))
barra_usuario.send_keys(telefono)
#CUMPLEAÑOS
time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "birthday")))
barra_usuario.send_keys(cumple)
#GENERO
time.sleep(1)
select_element = driver.find_element(By.NAME,'gender')
select_object = Select(select_element)
select_object.select_by_value('Male')
#DIRECCION 1
time.sleep(1)
barra_clave2 = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "address_1")))
barra_clave2.send_keys(direccion)
#CIUDAD
time.sleep(1)
barra_clave2 = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "city")))
barra_clave2.send_keys(ciudad)
#CODIGO POSTAL
time.sleep(1)
barra_clave2 = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "postcode")))
barra_clave2.send_keys(postal)
#CONTRASEÑA
time.sleep(1)
barra_clave2 = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "password")))
barra_clave2.send_keys(passes)
#CONFIRMAR CONTRASEÑA
time.sleep(1)
barra_clave2 = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "confirm")))
barra_clave2.send_keys(passes)
#POLITICAS
time.sleep(1)
driver.find_element(By.NAME, "agree").click()
#SUBMIT
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()

time.sleep(10)
driver.get("https://offspringinc.es/logout")
#Cerrar cookie
time.sleep(5)
driver.find_element(By.CLASS_NAME,"close").click()
time.sleep(4)

#-------------------------------------RECUPERAR CONTRASEÑA---------------------------------------------------------

driver.get("https://offspringinc.es/index.php?route=account/forgotten")
#Cerrar cookie
time.sleep(5)
driver.find_element(By.CLASS_NAME,"close").click()
time.sleep(3)

barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "email")))
barra_usuario.send_keys(mail.json()[0])


time.sleep(1)
driver.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()
time.sleep(5)

#-------------------------------CHEQUEO MAIL Y CAMBIO DE CONTRASEÑA-----------------------------------------
#LEER LOS MAILS BUSCANDO EL QUE PERMITE CONFIRMAR EL RESTABLECIMIENTO DE CONTRASEÑA
contenido = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+mail.json()[0].split("@")[0]+"&domain="+mail.json()[0].split("@")[1])

for i in contenido.json():
	if i["subject"] == "Offsping ES - Password reset request":
		ide = i["id"]

mail_confirmacion = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login="+mail.json()[0].split("@")[0]+"&domain="+mail.json()[0].split("@")[1]+"&id="+str(ide))
link=mail_confirmacion.json()['htmlBody'].replace('\n', "").replace('\r', "").split("href=")[2].split("style")[0]
link = link[1:-2].split("amp;")
link = "".join(link)
time.sleep(10)
confirmar = driver.get(link)
#Cerrar cookie
time.sleep(5)
driver.find_element(By.CLASS_NAME,"close").click()
time.sleep(5)

clave = random_pass()
print('Clave nueva: '+clave)
time.sleep(3)

print("CAMBIANDO CLAVE")
time.sleep(5)

barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_afilation.send_keys(clave)

time.sleep(1)
barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "confirm")))
barra_afilation.send_keys(clave)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()

time.sleep(10)


#-----------------------------------------LOGIN--------------------------------------------------------------

print("LOGEANDO")
driver.get("https://offspringinc.es/login")
#Cerrar cookie
time.sleep(5)
driver.find_element(By.CLASS_NAME,"close").click()

barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "email")))
barra_usuario.send_keys(mail.json()[0])

time.sleep(1)
barra_clave = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_clave.send_keys(clave)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"input[type='submit' i]").click()

time.sleep(10)

#--------------------------------------CAMBIAR CONTRASEÑA---------------------------------------------------

print("CAMBIANDO CONTRASEÑA")
#Cerrar cookie
time.sleep(5)
driver.find_element(By.CLASS_NAME,"close").click()

clave_nueva = random_pass()
print("clave nueva: "+clave_nueva)

time.sleep(1)
driver.find_element(By.ID, "password-reset-btn").click()

time.sleep(2)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID, "change-password-1")))
barra_usuario.send_keys(clave_nueva)
time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID, "change-password-2")))
barra_usuario.send_keys(clave_nueva)

time.sleep(10)
element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID, "password-save-btn"))).click()

print("LOGOUT")
time.sleep(3)
driver.get("https://offspringinc.es/logout")
time.sleep(4)

driver.close()
