from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


service_obj = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")          # parent to child xpath
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")    # parent to child CSS
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()              # normal xpath method
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()    # used text of the button for xpath

