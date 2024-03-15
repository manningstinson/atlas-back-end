#!/usr/bin/python3

import json

def organize_tasks(data):
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
    with open('todo_all_employees.json', 'r') as file:
        data = json.load(file)
    
    organized_data = organize_tasks(data)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(organized_data, file, indent=4)

if __name__ == "__main__":
    main()
