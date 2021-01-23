from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/pdf")
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", "D:\\Selenium with Python\\Selenium_Basics\\File Download")
profile.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(firefox_profile=profile)
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
