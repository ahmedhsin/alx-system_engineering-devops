#!/usr/bin/python3
"""scrip for gather data from an api"""

import requests as req
from sys import argv


def main():
    """entry point of script"""
    users_api = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    user = req.get(users_api).json()
    todos_api = f"https://jsonplaceholder.typicode.com/todos/"
    todos = req.get(todos_api).json()
    user_todos = []
    user_completed = []
    for todo in todos:
        if todo.get('userId') == user.get('id'):
            user_todos.append(todo)
            if todo.get('completed') is True:
                user_completed.append(todo)
    user_detials = "Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(user_completed), len(user_todos))
    print(user_detials)
    for todo in user_completed:
        print("\t {}".format(todo.get('title')))


if __name__ == '__main__':
    main()
