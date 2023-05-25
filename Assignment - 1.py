from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.find_element(By.XPATH, "//div/p[2]").text)
string = driver.find_element(By.XPATH, "//div/p[2]").text
str(string)
list = (string.split(" "))
print(list)
email = list[4]
print(email)
driver.close()
driver.switch_to.window(windows[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
