import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# name:Olaitan
# tool:python
# project:swaglab login functionality

driver.get("https://www.saucedemo.com/")

driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.CLASS_NAME, "submit-button").click()

# Section B:
# 1. Automate Add 5 items to Cart, remove the item 1, 3 and 5
# 2. Continue shopping, add two more items
# 3. Checkout button
# 4. Automate Log out
# 5. Close browser


# Automate Add 5 items to Cart, remove the item 1, 3 and 5
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
time.sleep(5)


driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()


driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-onesie"]').click()
driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="continue-shopping"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("olaitan")
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('ipadeola')
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(11111)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
driver.find_element(By.XPATH, '//*[@id="finish"]').click()





driver.implicitly_wait(10)
driver.maximize_window()

time.sleep(5)

driver.quit()


