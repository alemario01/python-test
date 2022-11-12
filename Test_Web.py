from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#given
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://www.python.org")

#assert "Python in driver.title"

#when
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("varible")

boton = driver.find_element(By.ID, "submit")
boton.click()
time.sleep(5)