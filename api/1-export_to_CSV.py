#!/usr/bin/python3
import csv
import json
import sys


def export_to_csv(user_id):
    with open('todos.json') as json_file:
        data = json.load(json_file)

    tasks = [task for task in data if task['userId'] == user_id]

    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': task['userId'],
                'USERNAME': data[0]['username'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_csv(int(user_id))
