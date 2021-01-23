from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

time.sleep(2)
driver.find_element_by_xpath("//div[@class='products']//div[@class='product']//div[@class='product-action']/button").click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[normalize-space()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element_by_class_name("promoCode").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()

# Explicit wait:
# waits for a certain condition to occur before proceeding further in the code.
wait = WebDriverWait(driver, 10)
wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

driver.quit()
