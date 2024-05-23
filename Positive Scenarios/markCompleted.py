from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Step 1: Open the to-do list webapp
driver.get("https://todomvc.com/examples/react/dist/")

# Wait for the page to load
time.sleep(2)

# Step 2: Locate the input field to add a new task
input_field = driver.find_element(By.CLASS_NAME, "new-todo")

# Step 3: Enter a valid task name (ex: Task 2)
task_name = "Task 2"
input_field.send_keys(task_name)

# Step 4: Hit the "Enter" button from the keyboard
input_field.send_keys(Keys.ENTER)

# Wait for the task to appear in the list
time.sleep(2)

# Step 5: Verify that the task appears in the to-do list
task_list = driver.find_elements(By.CLASS_NAME, "todo-list")
task_found = False
for task in task_list:
    if task_name in task.text:
        task_found = True
        break

assert task_found, f"Task '{task_name}' was not found in the to-do list."

# Step 6: Locate the checkbox next to the newly added task
checkbox = driver.find_element(By.XPATH, f"//label[text()='{task_name}']/preceding-sibling::input[@type='checkbox']")

# Step 7: Click the checkbox to mark the task as completed
checkbox.click()

# Wait for the task to be marked as completed
time.sleep(2)

# Step 8: Verify that the task is marked as completed
completed_task = driver.find_element(By.XPATH, f"//li[@class='completed']//label[text()='{task_name}']")
assert completed_task, f"Task '{task_name}' was not marked as completed."

print(f"The task '{task_name}' is marked as completed and its visual representation changes accordingly.")

# Close the browser
driver.quit()
