from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.find_element(By.CSS_SELECTOR, ".menu_Trains").click()
