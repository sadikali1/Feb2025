from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_remote():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Remote(
        command_executor="http://192.168.1.16:1234/wd/hub",
        options=chrome_options
    )

    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    driver.save_screenshot("screen.png")

    element = driver.find_element(By.CSS_SELECTOR,'a[data-testid="open-registration-form-button"]')
    element.screenshot("registration.png")


    # Request libray
    # Exception handling
    # CSS selector more examples
    # Git

