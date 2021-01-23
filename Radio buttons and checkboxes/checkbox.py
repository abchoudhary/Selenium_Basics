from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

# checkbox is checked or not
print(driver.find_element_by_id("checkBoxOption1").is_selected())
print(driver.find_element_by_id("checkBoxOption2").is_selected())

# Select checkboxes
driver.find_element_by_id("checkBoxOption1").click()
driver.find_element_by_id("checkBoxOption2").click()

print(driver.find_element_by_id("checkBoxOption1").is_selected())
print(driver.find_element_by_id("checkBoxOption2").is_selected())

driver.quit()
