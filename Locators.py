from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


service_obj = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# static dropdowns which have fixed values like Yes / No, Male / Female, Married / Unmarried etc.
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))  # Select class is used for static dropdowns
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value("Male")


# syntax for xpath = //tagname[@attribute='value']
# example xpath of submit button = //input[@type='submit']

# syntax for CSS selector = tagname[attribute='value']
# example CSS selector of name keyword = input[name='name']

# shortcuts for CSS selector = #id, .classname

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Pooja")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()          # CSS selector #id method
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Kale")    # index given as there were common values
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()





