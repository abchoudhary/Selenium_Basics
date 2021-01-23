from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

links = driver.find_elements_by_tag_name("a")

# Number of links on the page
print(len(links))

# print all the links
for link in links:
    print(link.text)

# clicking on the links
driver.find_element_by_link_text("Appium").click()
time.sleep(2)
print(driver.title)
driver.back()
time.sleep(2)

driver.find_element_by_partial_link_text("Free Access to InterviewQues").click()
print(driver.title)

driver.quit()
