#!/usr/bin/python3
"""scrip for gather data from an api"""

import json
import requests as req


def main():
    """entry point of script"""
    users_api = f"https://jsonplaceholder.typicode.com/users/"
    users = req.get(users_api).json()
    todos_api = f"https://jsonplaceholder.typicode.com/todos/"
    todos = req.get(todos_api).json()
    users_todos = {}
    users_ids = {}
    for user in users:
        users_ids[f"{user.get('id')}"] = user

    for todo in todos:
        user_id = f"{todo.get('userId')}"
        if user_id not in users_todos:
            users_todos[f"{todo.get('userId')}"] = []
        users_todos[user_id].append({
            'username': f"{users_ids[user_id].get('username')}",
            'task': todo.get('title'),
            'completed': todo.get('completed')
        })
    with open("todo_all_employees.json", mode='w') as file:
        json.dump(users_todos, file)


if __name__ == '__main__':
    main()
