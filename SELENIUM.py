
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # make sure ChromeDriver is installed
driver.get("https://demo.testfire.net/")

# Example: click "Sign In"
driver.find_element(By.LINK_TEXT, "Sign In").click()
time.sleep(2)

# Enter username & password
driver.find_element(By.ID, "uid").send_keys("admin")
driver.find_element(By.ID, "passw").send_keys("admin123")
driver.find_element(By.NAME, "btnSubmit").click()
