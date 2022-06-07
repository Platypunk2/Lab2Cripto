from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome(executable_path=r"/home/platypunk/Descargas/chromedriver101/chromedriver")

with open('password.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        driver.get("https://www.pclinkstore.cl/customer/login")
        time.sleep(5)
        email = row[0]
        contrase = row[1]
        driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[1]/input").send_keys(email)
        driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[2]/div/input").send_keys(contrase)
        driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/form/div/div[3]/input").click()
        time.sleep(10)

driver.close()