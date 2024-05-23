from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup the web driver (Chrome in this case)
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH

try:
    # Open the to-do list webapp
    driver.get("https://todomvc.com/examples/react/dist/")
    
    # Locate the input field to add a new task
    input_field = driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    
    # Enter a valid task name (e.g., Task 4) and hit the Enter key
    task_name = "Task 4"
    input_field.send_keys(task_name)
    input_field.send_keys(Keys.ENTER)
    
    time.sleep(2)  # Wait for the task to be added to the list
    
    # Verify that the task appears in the to-do list
    tasks = driver.find_elements(By.XPATH, f'//label[text()="{task_name}"]')
    assert len(tasks) > 0, f"Task '{task_name}' was not added to the list"
    
    # Locate the destroy button next to the newly added task
    destroy_button = driver.find_element(By.XPATH, f'//label[text()="{task_name}"]/following-sibling::button')
    
    # Click the destroy button to remove the task from the list
    driver.execute_script("arguments[0].click();", destroy_button)  # Using JavaScript click to avoid potential issues
    
    time.sleep(2)  # Wait for the task to be removed from the list
    
    # Verify that the task is removed
    tasks = driver.find_elements(By.XPATH, f'//label[text()="{task_name}"]')
    assert len(tasks) == 0, f"Task '{task_name}' was not removed from the list"

    print(f"The task '{task_name}' was successfully added and removed.")
    
finally:
    # Clean up and close the browser
    driver.quit()
