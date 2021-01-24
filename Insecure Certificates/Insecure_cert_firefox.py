from selenium import webdriver

# profile = webdriver.FirefoxProfile()
# profile.accept_untrusted_certs = True
# driver = webdriver.Firefox(firefox_profile=profile)

capabilities = webdriver.DesiredCapabilities.FIREFOX
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Firefox(desired_capabilities=capabilities)

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
