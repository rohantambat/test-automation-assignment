from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the to-do list webapp
driver.get("https://todomvc.com/examples/react/dist/")

try:
    # Wait for the input field to be visible
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "new-todo"))
    )
    
    # Enter a task name of only one random character or number
    input_field.send_keys("1")
    
    # Hit the "Enter" button
    input_field.send_keys(Keys.ENTER)
    
    # Wait for the task list to be updated
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ul[@class='todo-list']/li"))
    )
    
    # Find all tasks in the list
    tasks = driver.find_elements_by_xpath("//ul[@class='todo-list']/li")
    
    # Verify that no task is added to the to-do list with a length less than 2 characters
    assert len(tasks) == 0, "Task with less than 2 characters added to the list"
    
    print("No task with less than 2 characters added to the list as expected")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
