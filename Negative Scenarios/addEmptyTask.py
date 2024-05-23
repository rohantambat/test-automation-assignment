from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the to-do list webapp
driver.get("https://todomvc.com/examples/react/dist/")

# Wait for the page to load
time.sleep(2)

# Locate the input field to add a new task
input_field = driver.find_element(By.XPATH, '//input[@class="new-todo"]')

# Keep the input field blank and hit "Enter"
input_field.send_keys(Keys.ENTER)

# Wait for the task to be added (or not)
time.sleep(2)

# Verify that no task appears in the to-do list
todo_list_items = driver.find_elements(By.CSS_SELECTOR, '.todo-list li')
if len(todo_list_items) == 0:
    print("Test Passed: No task appears in the to-do list.")
else:
    print("Test Failed: Tasks were added to the to-do list.")

# Close the browser
driver.quit()
