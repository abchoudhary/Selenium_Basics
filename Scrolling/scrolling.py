from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(5)

# 1.Scrolling down the page by pixels
driver.execute_script("window.scrollBy(0,2000)", "")            # second argument is empty
time.sleep(3)

# 2. Scroll down the page till element is found
flag = driver.find_element_by_xpath("//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();", flag)
time.sleep(3)

# 3.Scroll down to the end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(3)

driver.quit()
