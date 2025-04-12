from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class TestSelenium:

    def test_selenium_alert(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/alerts")
        driver.find_element(By.ID, "alertButton").click()
        alert1 = Alert(driver)
        assert alert1.text == "You clicked a button"
        alert1.accept()
        element = driver.find_element(By.ID, "confirmButton")
        driver.execute_script("arguments[0].scrollIntoView(true)", element)
        element.click()
        Alert(driver).dismiss()
        element = driver.find_element(By.ID, "promtButton")
        driver.execute_script("arguments[0].scrollIntoView(true)", element)
        element.click()
        alert = Alert(driver)
        alert.send_keys("testing")
        alert.accept()

        driver.quit()


# Get
# click sendKeys
# Get elements methods
