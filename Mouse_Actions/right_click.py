from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.implicitly_wait(10)

actions = ActionChains(driver)

right_click_button = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
actions.context_click(right_click_button).perform()
time.sleep(2)

driver.quit()
