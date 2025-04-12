from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestDragDrop:

    def test_drag_drop(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/droppable")

        action = ActionChains(driver)
        source_element = driver.find_element(By.ID, 'draggable')
        target_element = driver.find_element(By.ID, 'droppable')
        action.drag_and_drop(source_element, target_element).perform()

    def test_drag_drop_position(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/dragabble")

        action = ActionChains(driver)
        source_element = driver.find_element(By.ID, 'dragBox')
        action.drag_and_drop_by_offset(source_element, 200, 50).perform()
