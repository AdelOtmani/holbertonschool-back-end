#!/usr/bin/python3
"""
Import modules requests for api data
"""
import requests
from sys import argv


def api():
    """
    Write a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    """
    url = requests.get("http://jsonplaceholder.typicode.com/users")
    for users in url.json():
        if users.get("id") == int(argv[1]):
            EMPLOYEE_NAME = (users.get("name"))
            break
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    TODO = requests.get("http://jsonplaceholder.typicode.com/todos")
    for TODOS in TODO.json():
        if TODOS.get("userId") == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if TODO.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(TODO.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for TASK in TASK_TITLE:
        print("\t {}".format(TASK))

if __name__ == "__main__":
    api()
