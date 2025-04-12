from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestIFrame:

    def test_handle_iframe(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/frames")
        text_message = driver.find_element(By.XPATH, "//div[@id='framesWrapper']/div").text
        assert text_message == "Sample Iframe page There are 2 Iframes in this page. Use browser inspecter or firebug to check out the HTML source. In total you can switch between the parent frame, which is this window, and the two frames below"

        driver.switch_to.frame('frame1')
        frame_text = driver.find_element(By.XPATH, '//h1[@id="sampleHeading"]').text
        assert frame_text == "This is a sample page"

        driver.switch_to.parent_frame()
        text_message = driver.find_element(By.XPATH, "//div[@id='framesWrapper']/div").text
        assert text_message == "Sample Iframe page There are 2 Iframes in this page. Use browser inspecter or firebug to check out the HTML source. In total you can switch between the parent frame, which is this window, and the two frames below"

    def test_handle_nested_iframe(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/nestedframes")
        text_message = driver.find_element(By.XPATH, "//div[@id='framesWrapper']/div[1]").text
        assert text_message == "Sample Nested Iframe page. There are nested iframes in this page. Use browser inspecter or firebug to check out the HTML source. In total you can switch between the parent frame and the nested child frame."

        driver.switch_to.frame('frame1')
        frame_text = driver.find_element(By.XPATH, '//body').text
        assert frame_text == "Parent frame"

        driver.switch_to.frame(0)
        child_frame_text = driver.find_element(By.XPATH, "//body/p").text
        assert child_frame_text == "Child Iframe"

        #driver.switch_to.parent_frame()
        #driver.switch_to.parent_frame()

        driver.switch_to.default_content()
        text_message = driver.find_element(By.XPATH, "//div[@id='framesWrapper']/div").text
        assert text_message == "Sample Nested Iframe page. There are nested iframes in this page. Use browser inspecter or firebug to check out the HTML source. In total you can switch between the parent frame and the nested child frame."

        '''
        By.ID
        By.NAME
        By.CLASS_NAME
        By.TAG_NAME
        By.LINK_TEXT
        By.PARTIAL_LINK_TEXT
        By.XPATH
        By.CSS_SELECTOR
        '''