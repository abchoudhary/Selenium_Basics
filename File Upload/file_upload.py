from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.guru99.com/test/upload/")
driver.implicitly_wait(5)

file_path = "/Web Tables\\table_data.xlsx"

driver.find_element_by_id("uploadfile_0").send_keys(file_path)
time.sleep(1)
driver.find_element_by_id("submitbutton").click()
time.sleep(2)

upload_success = driver.find_element_by_css_selector("h3[id='res'] center").is_displayed()
if upload_success:
    assert True, "File uploaded. Test Passed."
else:
    assert False, "File not uploaded. Test Failed"

driver.quit()
