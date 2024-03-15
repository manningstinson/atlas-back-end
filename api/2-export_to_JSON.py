#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress and export in JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    response = requests.get(
        f"{API_URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )

    if response.status_code != 200:
        print(f"RequestError: {response.status_code}")
        sys.exit(1)

    data = response.json()

    if not data:
        print(f"No tasks found for user ID {EMPLOYEE_ID}")
        sys.exit(1)

    user_tasks = []
    for task in data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        }
        user_tasks.append(task_dict)

    try:
        with open(f"{EMPLOYEE_ID}.json", "w") as file:
            json.dump(user_tasks, file)
        print("JSON export successful.")
    except Exception as e:
        print(f"Error occurred while exporting JSON: {e}")
