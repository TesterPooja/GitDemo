from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Testdemo:
    def test_gettestdemo(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        service_obj = Service("C:/Users/Pooja/Downloads/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=service_obj)
        driver.implicitly_wait(5)

        driver.maximize_window()
        driver.get("https://www.google.com/")
        driver.find_element(By.CSS_SELECTOR, ".gLFyf").send_keys("chennai")
        driver.find_element(By.XPATH, "//span[text()='Chennai Super Kings']").click()
