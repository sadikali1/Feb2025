import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestWindowHandle:

    @pytest.fixture
    def setup(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get("https://demoqa.com/browser-windows")
        yield
        self.driver.quit()


    def test_selenium_window(self, setup):
        self.driver.find_element(By.ID, "tabButton").click()
        parent_id = self.driver.current_window_handle
        win_ids = self.driver.window_handles
        for win_id in win_ids:
            self.driver.switch_to.window(win_id)

        window_text = self.driver.find_element(By.ID, "sampleHeading").text
        assert window_text == "This is a sample page"
        self.driver.close()
        self.driver.switch_to.window(parent_id)
        text1 = self.driver.find_element(By.XPATH , '//h1[@class="text-center"]').text
        assert text1 == "Browser Windows"
