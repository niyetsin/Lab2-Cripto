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


usuarios = ["solange.rodriguez","ivelisse.perez","victor.miranda","hernan.diaz","david.avalos","jessica.valdebenito","alonso.arellano","christian.vergara","omar.matus","juancarlos.gutierrez","marcela.rosinelli","oscar.olivos","roberto.castro","ester.vera","angela.garay","cristian.contreras","paola.gonzalez.f","rodrigo.calderon","claudio.osorio","eduardo.duran"]
claves = ["5330","9435","26732673","6528","oaw","9822","aab1060","8447","8169","1468","3850","8243","4588","7228","6417","7237","1985","6878","6182","0888"]


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
driver.switch_to.default_content()
driver.maximize_window()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')

for i in range(len(usuarios)):
	driver.get("https://pagosyserviciosenlinea.usach.cl/user/login")
	time.sleep(3)


	barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "login-form[login]")))
	barra_usuario.send_keys(usuarios[i])


	time.sleep(1)
	barra_clave = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "login-form[password]")))
	barra_clave.send_keys(claves[i])

	time.sleep(1)
	driver.find_element(By.CLASS_NAME, "checkbox").click()
	time.sleep(10)

driver.close()

