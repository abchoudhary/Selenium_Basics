# Selenium Basics
**Installation:**
```pip install selenium```

**Browser Drivers:**
* To avoid passing the executable path, keep the drivers in Scripts folder at location where python is installed and add the path of both Scripts folder and python folder to environment variables.
```
driver = webdriver.Chrome(executable_path="")
driver = webdriver.Firefox()
driver = webdriver.Ie()
```

**Input boxes:**
* Values in input boxes can be entered by using send_keys() method.

**Conditional Commands:**
```
is_displayed()
is_enabled()
is_selected()
```

**Navigational commands:**
```
driver.back()
driver.forward()
```

**Radio Buttons:**
* Count the number of radio buttons
  ```
  len(driver.find_elements_by_name("radioButton"))
  ```
* Check if the radio button is selected or not
  ```
  driver.find_element_by_xpath("xpath").is_selected()
  ```
* Select radio button
  ```
  driver.find_element_by_xpath("xpath").click()
  ```
**Checkboxes:**
* Check if the checkbox is checked or not
  ```
  driver.find_element_by_id("id").is_selected()
  ```
* Select checkbox
  ```
  driver.find_element_by_id("id").click()
  ```
**Dropdown:**
```
from selenium.webdriver.support.ui import Select
dropdown = Select(driver.find_element_by_id("")

dropdown.select_by_visible_text("text")
dropdown.select_by_value("value")
dropdown.select_by_index(index)
```
**Mouse Actions:**
```
from selenium.webdriver import ActionChains
actions = ActionChains(driver)
```
* double click:
    ```
    actions.double_click(element).perform()
    ```
* right click:
    ```
    actions.context_click(element).perform()
    ```
* drag and drop:
    ```
    actions.drag_and_drop(source, target).perform()
    ```
* mouse hover:
    ```
    actions.move_to_element(element1).move_to_element(element2).click().perform()
    ```
**Links:**
```
links = driver.find_elements_by_tag_name("a")

# Number of links on the page
print(len(links))

# print all the links
for link in links:
    print(link.text)
```
**Waits:**
* Implicit Wait: Checks the DOM for a certain amount of time when trying to find any element (or elements) not immediately available.
  ```
  driver.implicitly_wait(10)
  # This waits up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds.
  ```
* Explicit Wait: waits for a certain condition to occur before proceeding further in the code.
  ```
  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as ec
  
  wait = WebDriverWait(driver, 10)
  wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "class_name")))
  ```
**Data Driven Testing:**
```
pip install openpyxl
```
* Create a utility file to access data from Excel file.
    ```
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    sheet.max_row                                                       (returns row count)
    sheet.max_column                                                    (returns column count)
    return sheet.cell(row=row_num, column=col_num).value                (read data from excel file)
    sheet.cell(row=row_num, column=col_num).value = data                (write data to excel file)
    workbook.save(file)                                                 (save updated file)
    ```
**Alerts:**
```
driver.switch_to.alert.accept()                 (accept the alert by pressing OK)
driver.switch_to.alert.dismiss()                (dismiss the alert by pressing Cancel)
driver.switch_to.alert.text                     (get the text from alert)
```
**Frames:**
```
driver.switch_to.frame(locator)                 (switch to frame)
driver.switch_to.default_content()              (switch back to main window)
```
**Multiple Browser Windows**
```
driver.current_window_handle                    (get current window handle)
driver.window_handles                           (get all window handles)

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
driver.close()
```
**Web Tables:**
* Get the row and column count by identifying rows and columns using xpath.
* Run a for loop for both rows and columns(leave the header out for rows, start loop from 2).
```
row_count = len(driver.find_elements_by_xpath("//table/tbody/tr"))
col_count = len(driver.find_elements_by_xpath("//table/tbody/tr/th"))

for row in range(2, row_count+1):
    for col in range(1, col_count+1):
        data = driver.find_element_by_xpath("//table/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
        print(data, end="   ")
    print()
```
**Scrolling:**
* Scrolling down the page by pixels
  ```
  driver.execute_script("window.scrollBy(0,2000)", "")
  ```
* Scroll down the page till element is found
  ```
  driver.execute_script("arguments[0].scrollIntoView();", element)
  ```
* Scroll down to the end of the page
  ```
  driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
  ```
**Screenshots:**
* driver.save_screenshot("path")
* driver.get_screenshot_as_file("path")

**Cookies:**
* Get all cookies:
  ```
  driver.get_cookies()
  len(driver.get_cookies())
  ```
* Add a new cookie:
  ```
  cookie = {'name': 'MyCookie', 'value': '1234567890'}
  driver.add_cookie(cookie)
  ```
* deleting a cookie:
  ```
  driver.delete_cookie("MyCookie")
  ```
* deleting all cookies
  ```
  driver.delete_all_cookies()
  ```
**Logging:**
```
import logging
logging.basicConfig(
    filename="D:\\Selenium with Python\\Selenium_Basics\\Logging\\automation.log",
    format="%(asctime)s : %(levelname)s : %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG
)
logging.info("This is an INFO message")

OR

import logging
logging.basicConfig(
    filename="D:\\Selenium with Python\\Selenium_Basics\\Logging\\automation.log",
    format="%(asctime)s : %(levelname)s : %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p"
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info("This is an info message")
```
