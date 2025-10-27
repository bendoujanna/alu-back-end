#!/usr/bin/python3

"""
Module that returns information about an employee's TODO list progress
using the JSONPlaceholder REST API.
"""

import requests
import sys

if __name__ == "__main__":
    """
    Fetches and displays TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee whose data will be retrieved.

    Returns:
        None. Prints the employee's progress and completed tasks.
    """
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    
    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    employee_name = user.get("name")
    done_tasks = [for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))
    
    for task in done_tasks:
        print("\t {}".format(task.get("title")))