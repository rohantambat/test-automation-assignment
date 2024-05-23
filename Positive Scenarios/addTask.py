from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver for Chrome
driver = webdriver.Chrome()

try:
    # Open the to-do list webapp
    driver.get("https://todomvc.com/examples/react/dist/")

    # Wait for the page to load and input field to be visible
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "new-todo")))

    # Enter a valid task name and hit "Enter"
    task_name = "Task 1"
    input_field.send_keys(task_name)
    input_field.send_keys(Keys.ENTER)

    # Verify that the task appears in the to-do list
    to_do_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "todo-list")))
    tasks = to_do_list.find_elements(By.TAG_NAME, "li")
    assert any(task_name in task.text for task in tasks), "Task was not added to the to-do list"

    # Verify the to-do list items count text and other UI elements
    footer = driver.find_element(By.CLASS_NAME, "footer")
    count_text = footer.find_element(By.CLASS_NAME, "todo-count")
    all_link = footer.find_element(By.LINK_TEXT, "All")
    active_link = footer.find_element(By.LINK_TEXT, "Active")
    completed_link = footer.find_element(By.LINK_TEXT, "Completed")
    clear_completed_button = footer.find_element(By.CLASS_NAME, "clear-completed")

    assert count_text.is_displayed(), "Count text is not displayed"
    assert all_link.is_displayed(), "All link is not displayed"
    assert active_link.is_displayed(), "Active link is not displayed"
    assert completed_link.is_displayed(), "Completed link is not displayed"
    assert clear_completed_button.is_displayed(), "Clear completed button is not displayed"


    print("Test passed: The task is added and UI elements are verified.")
except AssertionError as e:
    print(f"Test failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the WebDriver
    driver.quit()
