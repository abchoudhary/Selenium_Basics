from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

actions = ActionChains(driver)

dbl_click_button = driver.find_element_by_xpath("//button[normalize-space()='Copy Text']")
actions.double_click(dbl_click_button).perform()
time.sleep(2)

driver.quit()
