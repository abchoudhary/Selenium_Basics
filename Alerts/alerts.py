from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(5)

driver.find_element_by_id("name").send_keys("accept")
time.sleep(1)
driver.find_element_by_id("alertbtn").click()
time.sleep(2)

print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()

driver.find_element_by_id("name").send_keys("dismiss")
time.sleep(1)
driver.find_element_by_id("confirmbtn").click()
time.sleep(2)

print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

driver.quit()
