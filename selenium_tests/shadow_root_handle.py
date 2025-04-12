import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestShadowRoot:

    def test_shadow_root(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.timeouts.implicit_wait = 10
        driver.maximize_window()
        driver.get("https://watir.com/examples/shadow_dom.html")
        time.sleep(10)
        shadow_element = driver.find_element(By.ID, "shadow_host").shadow_root

        text = shadow_element.find_element(By.CSS_SELECTOR, 'span[id="shadow_content"] > span').text
        assert text == "some text"

