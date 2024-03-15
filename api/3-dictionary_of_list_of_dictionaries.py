#!/usr/bin/python3
"""
Module documentation for retrieving data in JSON format.
"""

import requests
import json

URL_BASE = 'https://jsonplaceholder.typicode.com/users/'


def retrieve_data():
    """
    Retrieves data from the API and writes it to a JSON file.
    """
    users = requests.get(URL_BASE).json()
    data = {}

    for user in users:
        user_id = user['id']
        tasks = requests.get(URL_BASE + str(user_id) + '/todos/').json()

        user_tasks = []
        for task in tasks:
            task_info = {
                'task': task['title'],
                'completed': task['completed'],
                'username': user['username']
            }
            user_tasks.append(task_info)

        data[user_id] = user_tasks

    with open('todo_all_employees.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    retrieve_data()
