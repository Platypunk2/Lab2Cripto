from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GenMail import *
import csv
import time
from CredecialesBasicas import *
from GuardarDat import *

driver = webdriver.Chrome(executable_path=r"/home/platypunk/Descargas/chromedriver101/chromedriver")
driver.get("https://www.zavvi.es/accountHome.account")

with open('genES.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        email = row[0]


driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div[1]/section/div/div[1]/div/form/div[4]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div[1]/section/div/div[1]/div/form/div[2]/div/div[1]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div[1]/section/div/div[1]/div/form/div[3]/div/button").click()
driver.save_screenshot("Prueba/OlvES01.png")
time.sleep(5)
driver.get(ObtenerLinkES(email))

newcon=GenPassword()

driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/form/div[2]/div/div/div[1]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/form/div[3]/div/div[1]/div[1]/input").send_keys(newcon)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/form/div[3]/div/div[2]/div/input").send_keys(newcon)
driver.save_screenshot("Prueba/OlvES02.png")
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/form/div[4]/div/div").click()
GuardarInfoES(email, newcon)
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/main/div[1]/div[2]/form/button").click()
time.sleep(5)

driver.get("https://www.zavvi.es/accountHome.account")
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[2]/div/div/div[1]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[3]/div/div/div[1]/input").send_keys(newcon)
driver.save_screenshot("Prueba/PaginaLog.png")
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[5]/div/button").click()
time.sleep(5)
driver.close()

#print(readMails(email))