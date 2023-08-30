from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

BrowserSortedList = []     # creating an empty list

# clicking on UI sort column header, also skipping below step can crosscheck assertion error
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

VegElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in VegElements:
    BrowserSortedList.append(element.text)      # extracting text from the elements into browser list

print(BrowserSortedList)       # this is browser sorted list by selenium UI operation

OriginalBrowserSortedList = BrowserSortedList.copy()    # copying browser sorted list as will sort it by python
print(OriginalBrowserSortedList)

BrowserSortedList.sort()        # sorting browser sorted list
print(BrowserSortedList)

# BrowserSortedList.reverse()     # one of the debug method to check if assertion fails if data is reversed
# print(BrowserSortedList)

assert OriginalBrowserSortedList == BrowserSortedList