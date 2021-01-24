from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--ignore-certificate-errors")
# driver = webdriver.Chrome(options=chrome_options)

capabilities = webdriver.DesiredCapabilities.CHROME
capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(desired_capabilities=capabilities)

driver.maximize_window()
driver.get("https://cacert.org/")

logo = driver.find_element_by_xpath("//div[@id='pageLogo']/a/img")
if logo.is_displayed():
    assert True
    print("Insecure certificate accepted, website logo displayed.")
else:
    print("Insecure certificate not accepted")
    assert False

driver.quit()
