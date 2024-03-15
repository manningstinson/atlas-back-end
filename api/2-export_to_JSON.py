#!/usr/bin/python3
"""
Script to retrieve task data from a REST API based on a given user ID,
and export it to both JSON and CSV files.
"""

import json
import csv
import requests
import sys


def export_to_json(user_id, data):
    """
    Export task data to a JSON file.

    Args:
        user_id (int): The ID of the user.
        data (list): List of task data.

    Returns:
        None
    """
    with open(f"{user_id}.json", "w") as json_file:
        json.dump({user_id: data}, json_file, indent=4)


def export_to_csv(user_id, data):
    """
    Export task data to a CSV file.

    Args:
        user_id (int): The ID of the user.
        data (list): List of task data.

    Returns:
        None
    """
    with open(f"{user_id}.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in data:
            writer.writerow([user_id, task["username"], str(task["completed"]), task["title"]])


def main():
    """
    Main function to retrieve task data for a user ID
    and export it to JSON and CSV files.
    """
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {sys.argv[0]} <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    API_URL = "https://jsonplaceholder.typicode.com"

    response = requests.get(f"{API_URL}/users/{user_id}/todos", params={"_expand": "user"})

    if response.status_code != 200:
        print(f"RequestError: {response.status_code}")
        sys.exit(1)

    data = response.json()

    if not data:
        print(f"No tasks found for user ID {user_id}")
        sys.exit(1)

    export_to_json(user_id, data)
    export_to_csv(user_id, data)


if __name__ == "__main__":
    main()
