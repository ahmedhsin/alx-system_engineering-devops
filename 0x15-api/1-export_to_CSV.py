#!/usr/bin/python3
"""scrip for gather data from an api"""

import csv
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
            user_todos.append(todo)

    with open("USER_ID.csv", mode='w') as file:
        user_writer = csv.writer(
            file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for todo in user_todos:
            user_writer.writerow([f"{user.get('id')}",
                                  f"{user.get('username')}",
                                  f"{todo.get('completed')}",
                                  f"{todo.get('title')}"])


if __name__ == '__main__':
    main()
