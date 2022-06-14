import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\data\sk\softwares\chromedriver.exe")
driver.get("http://localhost:8080/bookmydoc/")
driver.maximize_window()
print(driver.title)
#time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="leftcolumn"]/div/li[3]/a')
element.click()
element = driver.find_element(By.NAME, "id")
element.send_keys("10000")
time.sleep(5)
element = driver.find_element(By.NAME, "password")
element.send_keys("password")
element = driver.find_element(By.NAME, "login")
element.click()
element = driver.find_element(By.XPATH, '//*[@id="navlist"]/li[5]/a')
element.click()
time.sleep(2)

element = driver.find_element(By.NAME, "logout")
#element = driver.find_element(By.ID, "id")
element.click()
print("hi")



#driver.close()

