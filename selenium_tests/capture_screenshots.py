from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_capture_screenshot():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    driver.save_screenshot("screen.png")

    element = driver.find_element(By.CSS_SELECTOR,'a[data-testid="open-registration-form-button"]')
    element.screenshot("registration.png")
