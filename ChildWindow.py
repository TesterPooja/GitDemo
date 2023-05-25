from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows = driver.window_handles      # window_handles property shows open windows in list
driver.switch_to.window(windows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windows[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

