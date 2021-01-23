# Selenium Basics
**Installation:**
```pip install selenium```

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