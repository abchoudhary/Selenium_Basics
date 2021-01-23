from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)

driver.save_screenshot("D:\\Selenium with Python\\Selenium_Basics\\Screenshots\\screenshot1.png")

driver.get_screenshot_as_file("D:\\Selenium with Python\\Selenium_Basics\\Screenshots\\screenshot2.png")

driver.quit()
