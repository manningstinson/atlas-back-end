#!/usr/bin/python3
"""
Export data from an API endpoint to JSON format.
"""

import sys
import json
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/users/'

def export_to_json(user_id):
    """
    Retrieve tasks owned by a user from the API and export to JSON.

    Args:
        user_id (int): The ID of the user whose tasks will be retrieved.
    """
    user_url = f"{BASE_URL}{user_id}"
    todos_url = f"{BASE_URL}{user_id}/todos/"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Failed to retrieve data from the API.")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    tasks = []
    for todo in todos_data:
        task = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user_data["username"]
        }
        tasks.append(task)

    output_filename = f"{user_id}.json"
    with open(output_filename, 'w') as file:
        json.dump({str(user_id): tasks}, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_json.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    export_to_json(user_id)
