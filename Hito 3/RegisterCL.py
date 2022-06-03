from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GuardarDat import *
import time
from CredecialesBasicas import *
from GenMail import generateEmail

email= generateEmail()
telefono = GenNombre()
contrase = GenPassword()

driver = webdriver.Chrome(executable_path=r"/home/platypunk/Descargas/chromedriver101/chromedriver")
driver.get("https://www.pclinkstore.cl/customer/registration")
time.sleep(5)

driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/div/div[1]/div[1]/div/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/div/div[1]/div[2]/div/input").send_keys(telefono)
driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/div/div[3]/div[1]/div/input").send_keys(contrase)
driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/div/div[3]/div[2]/div/input").send_keys(contrase)
driver.save_screenshot("Prueba/RegCL.png")
driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/div/div[4]/input").click()
time.sleep(10)
driver.close()
GuardarInfoCL(email, contrase)