from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC

class TestTable:

    def test_wait(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.timeouts.implicit_wait = 10
        driver.get("https://demoqa.com/dynamic-properties")

        text = driver.find_element(By.ID, "visibleAfter").text
        assert text == "Visible After 5 Seconds"

    def test_wait_explicit(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.timeouts.implicit_wait = 10
        driver.get("https://demoqa.com/alerts")

        driver.find_element(By.ID, "timerAlertButton").click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.alert_is_present())

        alert1 = Alert(driver)
        assert alert1.text == "This alert appeared after 5 seconds"
        alert1.accept()





