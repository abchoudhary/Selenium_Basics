from selenium import webdriver
import excel_utils
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/auth/login")

file = "/Data Driven\\login.xlsx"

rows = excel_utils.get_row_count(file, 'Sheet1')
cols = excel_utils.get_col_count(file, 'Sheet1')

for row in range(2, rows+1):
    username = excel_utils.read_data(file, 'Sheet1', row, 1)
    password = excel_utils.read_data(file, 'Sheet1', row, 2)

    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

    if driver.title == "OrangeHRM":
        excel_utils.write_data(file, 'Sheet1', row, 3, 'Passed')
    else:
        excel_utils.write_data(file, 'Sheet1', row, 3, 'Failed')

    driver.back()
    driver.find_element_by_id("txtUsername").clear()
    driver.find_element_by_id("txtPassword").clear()
    time.sleep(2)

driver.quit()
