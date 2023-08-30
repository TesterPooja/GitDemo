from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://www.makemytrip.com/")
# driver.find_element(By.CLASS_NAME, "ic_circularclose_grey").click()
# driver.find_element(By.XPATH, "div[class='bgGradient webpSupport landingPageBg']").click()   # background click
driver.find_element(By.CSS_SELECTOR, ".menu_Trains").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, "Pune"))
driver.find_element(By.LINK_TEXT, "Pune").click()

