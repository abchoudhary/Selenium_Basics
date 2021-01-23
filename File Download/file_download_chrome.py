from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs",
    {"download.default_directory": "D:\\Selenium with Python\\Selenium_Basics\\File Download"}
)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.implicitly_wait(5)

# Download the text file
driver.find_element_by_id("textbox").send_keys("Text file download testing")
driver.find_element_by_id("createTxt").click()
time.sleep(1)
driver.find_element_by_id("link-to-download").click()
time.sleep(3)

# Download the pdf file
driver.find_element_by_id("pdfbox").send_keys("PDF file download testing")
driver.find_element_by_id("createPdf").click()
time.sleep(1)
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(3)

driver.quit()
