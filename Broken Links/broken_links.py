from selenium import webdriver
import requests

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.implicitly_wait(5)

links = driver.find_elements_by_tag_name('a')
broken_links = 0
working_links = 0

for link in links:
    attr = link.get_attribute('href')
    req = requests.head(attr)
    if req.status_code >= 400:
        broken_links = len(attr)
    else:
        working_links = len(attr)

print(f"Number of broken links: {broken_links}")
print(f"Number of broken links: {working_links}")

driver.quit()
