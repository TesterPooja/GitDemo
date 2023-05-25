from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Pooja"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "input[value='Alert']").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert name in alert_text
alert.accept()
# alert.dismiss()             to click on cancel or rejection of popup

