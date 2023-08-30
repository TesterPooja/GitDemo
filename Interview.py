

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service_obj = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options= options, service= service_obj)

driver.get("https://www.google.com/")
driver.find_element(By.XPATH, "JDNDG").send_keys("Pooja")
driver.find_element(By.XPATH, "JDNDG").send_keys("Pooja")
driver.find_element(By.ID, "submit").click()





