from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Open the to-do list webapp
    driver.get("https://todomvc.com/examples/react/dist/")

    # Wait for the page to load
    time.sleep(2)

    # Locate the input field to add a new task
    input_field = driver.find_element(By.CLASS_NAME, "new-todo")

    # Enter a valid task name (ex: Task 3) and hit "Enter"
    task_name = "Task 3"
    input_field.send_keys(task_name)
    input_field.send_keys(Keys.ENTER)

    # Wait for the task to appear in the list
    time.sleep(2)

    # Verify that the task appears in the to-do list
    tasks = driver.find_elements(By.CLASS_NAME, "todo-list")
    task_found = False
    for task in tasks:
        if task_name in task.text:
            task_found = True
            break

    assert task_found, "Task was not added to the to-do list."

    # Locate the newly added task
    task_item = driver.find_element(By.XPATH, f"//label[text()='{task_name}']")

    # Double-click on the newly added task to edit it
    driver.execute_script("arguments[0].scrollIntoView(true);", task_item)
    driver.execute_script("var evt = document.createEvent('MouseEvents'); evt.initMouseEvent('dblclick', true, true, window); arguments[0].dispatchEvent(evt);", task_item)

    # Locate the editing input field (it becomes visible on double-click)
    edit_input = driver.find_element(By.CSS_SELECTOR, "input.edit")

    # Change the task name from "Task 3" to "Task 3 - Edited" and hit "Enter"
    new_task_name = "Task 3 - Edited"
    edit_input.clear()
    edit_input.send_keys(new_task_name)
    edit_input.send_keys(Keys.ENTER)

    # Wait for the task name to be updated
    time.sleep(2)

    # Verify that the task name is updated in the list
    updated_task_found = False
    updated_tasks = driver.find_elements(By.CLASS_NAME, "todo-list")
    for task in updated_tasks:
        if new_task_name in task.text:
            updated_task_found = True
            break

    assert updated_task_found, "Task name was not updated in the to-do list."

    print("Test passed: The task name was successfully updated.")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the WebDriver
    driver.quit()
