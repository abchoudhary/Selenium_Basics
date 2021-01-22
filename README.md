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
    sheet.max_row       (returns row count)
    sheet.max_column    (returns column count)
    return sheet.cell(row=row_num, column=col_num).value
    sheet.cell(row=row_num, column=col_num).value = data
    workbook.save(file)
    ```
    
