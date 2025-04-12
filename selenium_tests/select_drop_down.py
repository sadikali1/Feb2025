from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TestDropDown:

    def test_drop_down(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://www.facebook.com/")

        driver.find_element(By.LINK_TEXT, "Create new account").click()
        driver.find_element(By.NAME, "firstname").send_keys("testing")
        driver.find_element(By.NAME, "lastname").send_keys("testing")
        day_element = driver.find_element(By.ID, "day")
        select = Select(day_element)
        select.select_by_index(10)

        Select(driver.find_element(By.ID, "month")).select_by_value("8")
        Select(driver.find_element(By.ID, "year")).select_by_visible_text("2015")

# Dropdown, wait, handle buttons