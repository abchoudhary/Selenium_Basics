from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.ca/")
driver.implicitly_wait(5)

# Capture all cookies created by browser
cookies = driver.get_cookies()
print(cookies)

# print number of cookies
print(len(cookies))

# add new cookies
cookie = {'name': 'MyCookie', 'value': '1234567890'}
driver.add_cookie(cookie)

# deleting a cookie
driver.delete_cookie("MyCookie")

# deleting all cookies
driver.delete_all_cookies()

driver.quit()
