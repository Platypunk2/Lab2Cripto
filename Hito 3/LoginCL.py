from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GuardarDat import *
import time
from CredecialesBasicas import *
from GenMail import generateEmail

email= generateEmail()
nombre = GenNombre()
contrase = GenPassword()

driver = webdriver.Chrome(executable_path=r"/home/platypunk/Descargas/chromedriver101/chromedriver")
driver.get("https://www.pclinkstore.cl/customer/login")
time.sleep(5)

with open('genCL.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        email = row[0]
        contrase = row[1]
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[1]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[2]/div/input").send_keys(contrase)
driver.save_screenshot("Prueba/LogCL.png")
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[3]/input").click()
time.sleep(10)
driver.close()