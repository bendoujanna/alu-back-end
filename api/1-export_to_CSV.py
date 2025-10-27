#!/usr/bin/python3
"""
This module retrieves an employee's TODO list from the JSONPlaceholder API
and exports the data to a CSV file.

The script takes an employee ID as a command-line argument and creates a file
named <employee_id>.csv with the following format:

"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import requests
import sys

if __name__ == "__main__":
    """Main entry point of the script."""

    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    
    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    username = user.get("username")

    # file name
    filename = f"{employee_id}.csv"

    # Write to CSV file 

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

    print(f"Data exported to {filename}")   

    # employee_name = user.get("name")
    # done_tasks = [for task in todos if task.get("completed")]
    # total_tasks = len(todos)

    # print("Employee {} is done with tasks({}/{}):".format(
    #     employee_name, len(done_tasks), total_tasks))
    
    # for task in done_tasks:
    #     print("\t {}".format(task.get("title")))