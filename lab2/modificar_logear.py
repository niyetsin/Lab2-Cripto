from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #se hace envios POST
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


usuarios = "prueba"
claves = "clave"
def random_pass():
	letras = string.ascii_lowercase
	password = ( ''.join(random.choice(letras) for i in range(6)))	
	return password



clave_nueva = random_pass()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
driver.switch_to.default_content()
driver.maximize_window()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')


driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/index")
time.sleep(3)


barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "username")))
barra_usuario.send_keys(usuarios)


time.sleep(1)
barra_clave = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "password")))
barra_clave.send_keys(claves)

time.sleep(1)
driver.find_element(By.NAME, "remember").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "submit").click()


time.sleep(1)
driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/user/profile")

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

time.sleep(1)
driver.find_element(By.NAME, "submitFormButton").click()

driver.close()