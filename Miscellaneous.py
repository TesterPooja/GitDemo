from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)   # for browser to keep opened
# options.add_argument("headless")         # without opening browser script will execute
options.add_argument("--ignore-certificate-errors")     # will ignore certificate errors
options.add_argument("--start-maximized")     # maximize window function can be executed like this as well

service = Service("C:/Users/Pooja/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.execute_script("window.scrollBy(0,500);")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")  # to scroll till end of page

# driver.get_screenshot_as_file("endofpage.png")     # to get screenshot


