from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()                  # these 2 lines are to remain browser open
options.add_experimental_option('detach', True)


service_obj = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")    # https://www.google.com/
print(driver.title)            # website title
print(driver.current_url)
driver.refresh()
# driver.forward()
# driver.back()
print(driver.name)             # browser name
# driver.minimize_window()
# driver.close()

# For firefox browser
# service_obj = Service("C:/Users/Pooja/Downloads/chromedriver_win32/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

# For Microsoft Edge browser
# service_obj = Service("C:/Users/Pooja/Downloads/chromedriver_win32/msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)
