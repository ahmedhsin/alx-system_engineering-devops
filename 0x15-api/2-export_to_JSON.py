#!/usr/bin/python3
"""scrip for gather data from an api"""

import json
import requests as req
from sys import argv


def main():
    """entry point of script"""
    users_api = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    user = req.get(users_api).json()
    todos_api = f"https://jsonplaceholder.typicode.com/todos/"
    todos = req.get(todos_api).json()
    user_todos = []
    for todo in todos:
        if todo.get('userId') == user.get('id'):
            user_todos.append({
                'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': user.get('username')
            })
    user_json = {f"{user.get('id')}": user_todos}
    with open(f"{user.get('id')}.json", mode='w') as file:
        json.dump(user_json, file)


if __name__ == '__main__':
    main()
