from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service_obj = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.google.com/")
driver.switch_to.frame("callout")
driver.find_element(By.XPATH, "//button[@class='M6CB1c rr4y5c']").click()
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, ".gLFyf").send_keys("chennai")
driver.find_element(By.XPATH, "//span[text()='Chennai Super Kings']").click()








