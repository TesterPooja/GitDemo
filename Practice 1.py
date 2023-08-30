from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.google.com")
driver.switch_to.frame("callout")
driver.find_element(By.CLASS_NAME, "rr4y5c").click()
driver.switch_to.default_content()
driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("chennai")
driver.find_element(By.XPATH, "//span[text()='Chennai Super Kings']").click()
