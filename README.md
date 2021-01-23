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
