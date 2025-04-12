from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestMouseHover:

    def test_mouse_hover(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/hovers")

        action = ActionChains(driver)
        user2_element = driver.find_element(By.XPATH, '//div[@class="example"]/div[@class="figure"][2]')
        user2_profile_element = driver.find_element(By.XPATH, '//a[@href="/users/2"]')
        action.move_to_element(user2_element).pause(2).click(user2_profile_element).perform()

