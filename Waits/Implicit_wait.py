from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Checks the DOM for a certain amount of time when trying to find any element not immediately available.
# Implicit wait is applicable to all elements on the page

driver.implicitly_wait(10)

# This waits up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds.

driver.find_element(By.ID, "txtUsername").send_keys("admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

assert "OrangeHRM" in driver.title

driver.quit()
