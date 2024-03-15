#!/usr/bin/python3
"""
Script to gather data from an API about an employee's TODO list progress
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO
    list progress of the employee with the given ID
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employee_id)

    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No data found for employee ID:", employee_id)
        return

    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)
    user_response = requests.get(user_url)
    user_info = user_response.json()
    employee_name = user_info.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))

    for todo in completed_tasks:
        print("\t", todo['title'])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
