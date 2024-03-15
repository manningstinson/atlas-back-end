#!/usr/bin/python3

"""
This script organizes tasks from all
employees into a dictionary of lists of dictionaries
and exports the data in JSON format.
"""

import json


def organize_tasks(data):
    """
    Organizes tasks from all employees into a
    dictionary of lists of dictionaries.

    Args:
        data (list): A list of dictionaries containing task data.

    Returns:
        dict: A dictionary where keys are
        user IDs and values are lists of dictionaries
        containing task information.
    """
    organized_data = {}
    for record in data:
        user_id = record['userId']
        task_info = {
            "username": record['username'],
            "task": record['title'],
            "completed": record['completed']
        }
        if user_id in organized_data:
            organized_data[user_id].append(task_info)
        else:
            organized_data[user_id] = [task_info]
    return organized_data


def main():
    """
    Main function to read, organize, and export task data.
    """
    with open('todo_all_employees.json', 'r') as file:
        data = json.load(file)

    organized_data = organize_tasks(data)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(organized_data, file, indent=4)


if __name__ == "__main__":
    main()
