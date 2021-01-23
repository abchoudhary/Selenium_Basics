from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

# Get the table data and print in console
row_count = len(driver.find_elements_by_xpath("//div[@class='left-align']//table[@id='product']/tbody/tr"))
col_count = len(driver.find_elements_by_xpath("//div[@class='left-align']//table[@id='product']/tbody/tr/th"))

for row in range(2, row_count+1):
    for col in range(1, col_count+1):
        data = driver.find_element_by_xpath(
            "//div[@class='left-align']//table[@id='product']/tbody/tr["+str(row)+"]/td["+str(col)+"]"
        ).text
        print(data, end="            ")
    print()

# Get the table data and write to excel file
file = "D:\\Selenium with Python\\Selenium_Basics\\Web_Tables\\table_data.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook['Sheet1']

rows = len(driver.find_elements_by_xpath("//div[@class='tableFixHead']//table[@id='product']/tbody/tr"))
cols = len(driver.find_elements_by_xpath("//div[@class='tableFixHead']//table[@id='product']/thead/tr/th"))

for row in range(1, rows+1):
    for col in range(1, cols+1):
        data = driver.find_element_by_xpath(
            "//div[@class='tableFixHead']//table[@id='product']/tbody/tr["+str(row)+"]/td["+str(col)+"]"
        ).text
        sheet.cell(row=row, column=col).value = data
workbook.save(file)

driver.quit()
