from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GuardarDat import *
import time
from CredecialesBasicas import *
from GenMail import generateEmail
import csv

driver = webdriver.Chrome(executable_path=r"/home/platypunk/Descargas/chromedriver101/chromedriver")
driver.get("https://www.zavvi.es/accountHome.account")

with open('genES.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        email = row[0]
        contrase = row[1]

driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[2]/div/div/div[1]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[3]/div/div/div[1]/input").send_keys(contrase)
driver.save_screenshot("Prueba/RestES.png")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[5]/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/main/div[6]/div/div[3]/div").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/main/div/div[3]/div/div/div/form/fieldset/div[7]/input").send_keys(contrase)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/main/div/div[3]/div/div/div/form/fieldset/div[8]/input").send_keys(contrase+"1")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/main/div/div[3]/div/div/div/form/fieldset/div[9]/input").send_keys(contrase+"1")
driver.save_screenshot("Prueba/RestES.png")
GuardarInfoES(email, contrase+"1")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/main/div/div[3]/div/div/div/form/fieldset/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/main/div[1]/div[2]/form/button").click()
time.sleep(2)

driver.get("https://www.zavvi.es/accountHome.account")
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[2]/div/div/div[1]/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[3]/div/div/div[1]/input").send_keys(contrase+"1")
driver.save_screenshot("Prueba/PaginaLog.png")
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div/div[1]/div/form/div[5]/div/button").click()
time.sleep(5)
driver.close()