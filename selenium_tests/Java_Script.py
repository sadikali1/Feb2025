from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestJS:

    def test_execute_js(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")

        #driver.execute_script("window.scroll(1000, 1000)")

        element = driver.find_element(By.CSS_SELECTOR,'a[href="/shadowdom"]')
        #driver.execute_script("arguments[0].click()", element )
        driver.execute_script("arguments[0].scrollIntoView(true)", element)