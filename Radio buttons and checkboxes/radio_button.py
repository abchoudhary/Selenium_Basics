from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

# Count the number of radio buttons
print(len(driver.find_elements_by_name("radioButton")))

# Check if the radio button is checked or unchecked
print(driver.find_element_by_xpath("//input[@value='radio3']").is_selected())

# Select radio button
driver.find_element_by_xpath("//input[@value='radio3']").click()

print(driver.find_element_by_xpath("//input[@value='radio3']").is_selected())

driver.quit()
