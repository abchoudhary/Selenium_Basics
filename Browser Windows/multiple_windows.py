from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

driver.find_element_by_id("openwindow").click()

current_handle = driver.current_window_handle               # get current window handle
print(current_handle)

handles = driver.window_handles                             # get all window handles
print(handles)

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
driver.close()

# driver.find_element_by_id("opentab").click()
#
# tab_handles = driver.window_handles
# for handle in tab_handles:
#     driver.switch_to.window(handle)
#     print(driver.title)
# driver.close()

driver.quit()
