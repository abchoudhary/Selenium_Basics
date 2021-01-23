from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.implicitly_wait(5)

# Switch to first frame
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()

# Switch to main page
driver.switch_to.default_content()

# Switch to second frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()

# Switch to main page
driver.switch_to.default_content()

# Switch to the third frame
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("//div[@class='topNav']//a[normalize-space()='Deprecated']").click()
time.sleep(2)

text = driver.find_element_by_xpath("//h1[normalize-space()='Deprecated API']").is_displayed()
if text:
    assert True, "Deprecated API is present on the page"
else:
    assert False, "Deprecated API is not present on the page"

driver.quit()
