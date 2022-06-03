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
print(mail.json())

def random_mail():
	letras = string.ascii_lowercase
	mail = ( ''.join(random.choice(letras) for i in range(5))) + '@' + ( ''.join(random.choice(letras) for i in range(5)))	
	return mail

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


driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/user/register")
time.sleep(3)


time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "givenName")))
barra_usuario.send_keys(random_name())

time.sleep(1)
barra_afilation = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "affiliation")))
barra_afilation.send_keys(random_name())

time.sleep(1)
select_element = driver.find_element(By.ID,'country')
select_object = Select(select_element)
select_object.select_by_value('CL')

time.sleep(1)
barra_mail = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "email")))
barra_mail.send_keys(mail.json()[0])

time.sleep(1)
barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "username")))
barra_usuario.send_keys(random_name())

passes = random_pass()
time.sleep(1)
barra_clave = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_clave.send_keys(passes)
print(passes)

time.sleep(1)
barra_clave2 = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "password2")))
barra_clave2.send_keys(passes)

time.sleep(1)
driver.find_element(By.NAME, "privacyConsent").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "submit").click()



time.sleep(4)
driver.close()