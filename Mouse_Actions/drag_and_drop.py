from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

actions = ActionChains(driver)

source = driver.find_element_by_xpath("//div[@id='draggable']")
destination = driver.find_element_by_xpath("//div[@id='droppable']")
actions.drag_and_drop(source, destination).perform()

driver.quit()
