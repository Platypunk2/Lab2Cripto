from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GenMail import *
import csv
import time
from CredecialesBasicas import *
from GuardarDat import *

driver = webdriver.Chrome(executable_path=r"/home/platypunk/Descargas/chromedriver101/chromedriver")
driver.get("https://www.pclinkstore.cl/customer/login")
time.sleep(5)

driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[3]/p/a").click()
time.sleep(2)

with open('genCL.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        email = row[0]

driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[1]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[3]/input").click()
time.sleep(10)
driver.save_screenshot("Prueba/OlvCL01.png")
driver.get(ObtenerLinkCL(email))
time.sleep(10)
newcontra = GenPassword()
driver.find_element_by_xpath("/html/body/section[2]/div/div/div/form/div/div[1]/div/input").send_keys(newcontra)
driver.find_element_by_xpath("/html/body/section[2]/div/div/div/form/div/div[2]/div/input").send_keys(newcontra)
driver.save_screenshot("Prueba/OlvCL02.png")
driver.find_element_by_xpath("/html/body/section[2]/div/div/div/form/div/div[3]/input").click()
GuardarInfoCL(email, newcontra)
time.sleep(2)
driver.find_element_by_xpath("/html/body/header/div[1]/div/div/div[2]/div/div[2]/a/span").click()
time.sleep(2)
driver.get("https://www.pclinkstore.cl/customer/login")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[1]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[2]/div/input").send_keys(newcontra)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[3]/input").click()
time.sleep(5)
driver.close()

