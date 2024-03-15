#!/usr/bin/python3
"""
Module: export_to_CSV

This module provides functionality to export task data to a CSV file based on a given user ID.
"""

import csv
import json
import os
import sys


def export_to_csv(user_id):
    """
    Export tasks belonging to the specified user to a CSV file.

    Args:
        user_id (int): The ID of the user whose tasks are to be exported.

    Returns:
        None
    """
    # Ensure that todos.json file exists in the current directory or provide correct path
    if not os.path.exists('todos.json'):
        print("Error: todos.json file not found.")
        sys.exit(1)

    with open('todos.json') as json_file:
        data = json.load(json_file)

    # Check if there are tasks associated with the specified user ID
    tasks = [task for task in data if task['userId'] == user_id]
    if not tasks:
        print(f"No tasks found for user ID {user_id}.")
        sys.exit(1)

    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': task['userId'],
                'USERNAME': data[0]['username'],  # Assuming username is same for all tasks
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_csv(int(user_id))
