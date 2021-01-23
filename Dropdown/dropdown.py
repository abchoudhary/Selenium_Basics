from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)

speed_dropdown = Select(driver.find_element_by_id("speed"))
speed_dropdown.select_by_visible_text("Medium")
time.sleep(2)

file_dropdown = Select(driver.find_element_by_id("files"))
file_dropdown.select_by_value("3")
time.sleep(2)

number_dropdown = Select(driver.find_element_by_id("number"))
number_dropdown.select_by_index(2)
time.sleep(2)

# printing number of options
print(len(speed_dropdown.options))

# Capture options present in the dropdown
all_options = speed_dropdown.options
for option in all_options:
    print(option.text)

driver.quit()
