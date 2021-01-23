from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(10)

actions = ActionChains(driver)

hover_button = driver.find_element_by_xpath("//button[normalize-space()='Mouse Hover']")
reload_button = driver.find_element_by_xpath("//a[normalize-space()='Reload']")

actions.move_to_element(hover_button).move_to_element(reload_button).click().perform()
time.sleep(2)

driver.quit()
