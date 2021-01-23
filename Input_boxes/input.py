from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID, "txtUsername").clear()
time.sleep(1)
driver.find_element(By.ID, "txtUsername").send_keys("admin")

driver.find_element(By.ID, "txtPassword").clear()
time.sleep(1)
driver.find_element(By.ID, "txtPassword").send_keys("admin123")

driver.quit()
