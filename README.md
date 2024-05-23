
# To-Do List WebApp Testing Guide

## Introduction

This document outlines the test scenarios and strategies for verifying the main functionalities of the Lightweight To-Do List webapp. The goal is to ensure that the app works as expected by covering both positive and negative scenarios. 
This guide will detail the test cases, testing patterns, organization, and reporting mechanisms used in the testing process.

## Test Scenarios

### Positive Scenarios

1. **Add a Task**
   - **Steps:**
     1. Open the to-do list webapp (ex: https://todomvc.com/examples/react/dist/).
     2. Locate the input field to add a new task.
     3. Enter a valid task name (ex: Task 1).
     4. Hit the "Enter" button from keyboard.
     5. Verify that the task appears in the to-do list.
     6. Verify that to-to-list items count text appears with other All, Active, Completed and Clear completed links & 'X' icon to remove item.
   - **Expected Result:**
     - The task "Task 1" is added to the list and displayed correctly.
     - User is on the "All" tab and to-to-list items count text is added with other links such as All, Active, Completed and Clear completed links & 'X' icon to remove item.

2. **Mark a Task as Completed**
   - **Steps:**
     1. Open the to-do list webapp.
     2. Add a task (ex: Task 2).
     3. Locate the checkbox next to the newly added task.
     4. Click the checkbox to mark the task as completed.
     5. Verify that the task is marked as completed.
   - **Expected Result:**
     - The task "Task 2" is marked as completed and its visual representation changes accordingly (ex. strip to title).

3. **Editing a Task**
   - **Steps:**
     1. Open the to-do list webapp.
     2. Add a task (e.g., "Task 3").
     3. Double-click on newly added task to edit it.
     4. Change the task name to "Task 3 - Edited".
     5. Hit the "Enter" button from keyboard.
     6. Verify that the task name is updated in the list.
   - **Expected Result:**
     - The task name is updated to "Task 3 - Edited" in the to-do list.

4. **Deleting a Task**
   - **Steps:**
     1. Open the to-do list webapp.
     2. Add a task (e.g., "Task 4").
     3. Locate the remove button/icon next to the task.
     4. Click the remove button.
     5. Verify that the task is removed from the list.
   - **Expected Result:**
     - The task "Task 4" is deleted and no longer appears in the list.

5. **Other Scenarios**
   - **Validate the Items count gets updated when we add/remove items**
   - **Validate that when user marks an item as completed it is visible in 'Completed' tab**
   - **Validate that hen user clicks on 'Clear completed' link, an items which are completed gets cleared/removed from list**
   - **Validate that Select all functionality by clicking on the dropdown icon on input field when there is at least 1 item present**


### Negative Scenarios

1. **Add an Empty Task**
   - **Steps:**
     1. Open the to-do list webapp.
     2. Locate the input field to add a new task.
     3. Leave the input field empty and Hit the "Enter" button on keyboard.
     4. Verify the response.
   - **Expected Result:**
     - The app should display an error message indicating that the task name cannot be empty OR Npthing should be added/happen (in case error message is not configured).

2. **Add a Task with length less than 2 characters**
   - **Steps:**
     1. Open the to-do list webapp.
     2. Locate the input field to add a new task.
     3. Enter a value less than 2 characters (only one text/number) (ex: 5).
     4. Hit the "Enter" button from keyboard.
     5. Verify that the task do not appears in the to-do list.
   - **Expected Result:**
     - The app should prevent adding the task whose length is less than 2 characters.

3. **Add a Task with invalid input**
   - **Steps:**
     1. Open the to-do list webapp.
     2. Locate the input field to add a new task.
     3. Enter a value with length is 2 characters where first/last character is space.
     4. Hit the "Enter" button from keyboard.
     5. Verify that the task do not appears in the to-do list.
   - **Expected Result:**
     - The app should prevent adding the task whose length is 2 characters and first/last character is space.

4. **Editing a Task to an Empty Name**
   - **Steps:**
     1. Open the to-do list webapp.
     2. Add a task (ex: "New Task").
     3. Double-click on newly added task to edit it.
     4. Change the task name to Blank/less than 2 characters.
     5. Hit the "Enter" button from keyboard.
     6. Verify the response
   - **Expected Result:**
     - The app should display an error message indicating that the task name cannot be empty and should not save the change OR Npthing should be updated/happened (in case error message is not configured).

## Testing Patterns and Strategies

### Testing Patterns

1. **Boundary Value Analysis:**
   - Used to test the limits of the input fields (ex: minimum task length).

2. **Equivalence Partitioning:**
   - Used to divide input data into valid and invalid partitions for more effective testing.

3. **Error Guessing:**
   - Based on experience, anticipate common errors that might occur (ex: adding an empty task).

4. **State Transition Testing:**
   - Verify the behavior of the app as it transitions from one state to another (ex: from active to completed tasks).

### Test Organization

- **Test Suites:** Organized by functionality (e.g., adding tasks, editing tasks, removing tasks etc).
- **Test Cases:** Each test case is detailed with steps, expected results, and actual results.
- **Priority Levels:** Tests can be prioritized based on their criticality to core functionalities.

### Reporting

- **Test Execution Reports:** Generated after each test run, detailing which tests passed, failed, not executed or were blocked.
- **Bug Reports:** for a raised bugs, generate report with detailed steps to reproduce, severity, and screenshots.
- **Summary Reports:** Summarize overall test coverage, number of test cases executed, passed, failed, and the health of the application.

## Conclusion

This document provides a comprehensive guide to testing the To-Do List webapp, ensuring thorough coverage of both positive and negative scenarios. Following the outlined strategies and patterns will help in identifying potential issues and ensuring a high-quality application. Regular reporting and documentation will facilitate effective communication and prompt resolution of any defects found.


