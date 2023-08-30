from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


service = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)      # implicit wait written after creating driver object

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)     # here used this method because selenium will not know what to return apart from list data type
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
count = len(results)
assert count > 0

# assignment of lists verification
expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []

for result in results:             # loop is to click on 3 buttons of add to cart
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()      # chaining mechanism to search element

print(actualList)
assert actualList == expectedList

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(2)       # do not not use here, use implicit wait globally
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)    # explicit wait for single element to show up if taking more time than implicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
text = driver.find_element(By.CLASS_NAME, "promoInfo").text
assert text == "Code applied ..!"

# sum validation

amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p[@class='amount']")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)

print(sum)

totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert sum == totalAmount

# assignment of discountAmount
discountAmount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert discountAmount < totalAmount










