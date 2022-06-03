from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GuardarDat import *
import time
from CredecialesBasicas import *
from GenMail import generateEmail

email= generateEmail()
nombre = GenNombreES()
contrase = GenPassword()

driver = webdriver.Chrome(executable_path=r"/home/platypunk/Descargas/chromedriver101/chromedriver")
driver.get("https://www.zavvi.es/accountCreate.account")

driver.find_element_by_xpath("/html/body/div[1]/div[5]/header/div[1]/section/div/div/div[2]/div/button").click()

driver.find_element_by_xpath("/html/body/div/div[5]/main/div/div/section/div[2]/form/div[2]/div/div/input").send_keys(nombre)
driver.find_element_by_xpath("/html/body/div/div[5]/main/div/div/section/div[2]/form/div[3]/div[1]/div/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div[2]/form/div[3]/div[2]/div/input").send_keys(email)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div[2]/form/div[4]/div[1]/div[1]/input").send_keys(contrase)
#driver.execute_script("window.scrollTo(100,document.body.scrollHeight)")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div[2]/form/div[4]/div[2]/div/input").send_keys(contrase)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div[2]/form/div[6]/div/div[3]/div/div/div/div/div[2]/label/span").click()
GuardarInfoES(email, contrase)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div/div/section/div[2]/form/div[7]/div[1]/div").click()
time.sleep(5)
driver.close()