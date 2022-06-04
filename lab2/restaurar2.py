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


mail = "probando@gmail.com"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
driver.switch_to.default_content()
driver.maximize_window()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')


driver.get("https://forums.overclockers.co.uk/lost-password/")
time.sleep(3)


barra_correo = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "email")))
barra_correo.send_keys(mail)

time.sleep(15)
barra_clave = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "login")))
barra_clave.send_keys(usuarios)

time.sleep(1)
driver.find_element(By.CLASS_NAME, "button--primary button").click()

driver.close()