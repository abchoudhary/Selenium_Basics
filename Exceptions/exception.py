from selenium import webdriver
from selenium.common.exceptions import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
driver.implicitly_wait(5)

try:
    element = driver.find_element_by_link_text("test")
    print(element.is_displayed())
except NoSuchElementException as err:
    print("No such element is present")

driver.quit()
