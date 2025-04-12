from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestCheckBox:

    def test_handle_iframe(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/checkbox")

        status = driver.find_element(By.XPATH, "//input[@id='tree-node-home']").is_selected()
        assert status == False
        driver.find_element(By.XPATH, "//span[text()='Home']").click()

        status = driver.find_element(By.XPATH, "//input[@id='tree-node-home']").is_selected()
        assert status == True
