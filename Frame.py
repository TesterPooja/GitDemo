from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT, "iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("Pooja is able to automate web")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
