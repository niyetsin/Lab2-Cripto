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
import requests
'''
mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
print(mail.json())
'''
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
driver.switch_to.default_content()
driver.maximize_window()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')


driver.get("http://ediciones.ucsh.cl/index.php/ForoEducacional/login/lostPassword")
time.sleep(3)


barra_usuario = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.NAME, "email")))
barra_usuario.send_keys('z7zjfrpj@bheps.com')


time.sleep(1)
driver.find_element(By.CLASS_NAME, "submit").click()
time.sleep(1)

driver.close()