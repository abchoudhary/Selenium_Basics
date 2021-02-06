from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www1.nseindia.com/products/content/derivatives/equities/archieve_fo.htm")
driver.implicitly_wait(5)

date_picker = driver.find_element_by_xpath("//input[@id='date']")
date_picker.click()
time.sleep(2)

select_month = driver.find_element_by_xpath("//select[@class='ui-datepicker-month']")
for option in select_month.find_elements_by_tag_name('option'):
    if option.text == "May":
        option.click()
        break

select_year = driver.find_element_by_xpath("//select[@class='ui-datepicker-year']")
for option in select_year.find_elements_by_tag_name('option'):
    if option.text == "2020":
        option.click()
        break

days = driver.find_elements_by_xpath("//a[@class='ui-state-default']")
for day in days:
    if day.text == '10':
        day.click()
        break

time.sleep(3)
driver.quit()

