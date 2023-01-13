import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.saucedemo.com/")

driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.CLASS_NAME, "submit-button").click()

driver.implicitly_wait(5)
driver.maximize_window()

time.sleep(5)

