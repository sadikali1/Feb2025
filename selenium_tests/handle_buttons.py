from argparse import Action

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class TestButtons:

    def test_handle_buttons(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/buttons")

        action = ActionChains(driver)
        button_element = driver.find_element(By.ID, "doubleClickBtn")
        action.double_click(button_element).perform()
        assert  driver.find_element(By.ID, "doubleClickMessage").text == "You have done a double click"

        action.context_click(driver.find_element(By.ID, "rightClickBtn")).perform()
        assert driver.find_element(By.ID, "rightClickMessage").text == "You have done a right click"

        action.click(driver.find_element(By.XPATH, "//button[text()='Click Me']")).perform()
        assert driver.find_element(By.ID, "dynamicClickMessage").text == "You have done a dynamic click"