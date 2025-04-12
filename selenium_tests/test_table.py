from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class TestTable:

    def test_table(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        driver.get("https://demoqa.com/webtables")

        driver.find_element(By.ID, "addNewRecordButton").click()
        driver.find_element(By.ID, "firstName").send_keys("Raj")
        driver.find_element(By.ID, "lastName").send_keys("Kumar")
        driver.find_element(By.ID, "userEmail").send_keys("Raj.kumar@test.com")
        driver.find_element(By.ID, "age").send_keys("50")
        driver.find_element(By.ID, "salary").send_keys("2097097097")
        driver.find_element(By.ID, "department").send_keys("QA Engineer")
        driver.find_element(By.ID, "submit").click()

        emails = driver.find_elements(By.XPATH, "//div[@class='rt-table']/div[@class='rt-tbody']/div/div/div[4]")
        for i in range(0, len(emails)):
            email = driver.find_element(By.XPATH, f"//div[@class='rt-table']/div[@class='rt-tbody']/div[{i}]/div/div[4]").text
            print(email)