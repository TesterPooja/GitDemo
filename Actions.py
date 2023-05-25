from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()      # to right-click

action.click(driver.find_element(By.LINK_TEXT, "Reload")).perform()
# OR
# action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

# some more methods below
# action.double_click(driver.find_element())
# action.drag_and_drop()


