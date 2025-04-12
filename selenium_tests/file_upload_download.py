from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestUploadDownload:

    def test_upload_down(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/upload-download")

        driver.find_element(By.ID, "downloadButton").click()
        driver.find_element(By.ID, "uploadFile").send_keys("C:\\Users\\pc\\Downloads\\sampleFile.jpeg")