#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = requests.get("http://jsonplaceholder.typicode.com/users")
    TODO = requests.get("http://jsonplaceholder.typicode.com/todos")
    Data = url.json()
    Data2 = TODO.json()
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for users in Data:
        if users.get("id") == int(argv[1]):
            EMPLOYEE_NAME = (users.get("name"))
  
    for TODOS in Data2:
        if TODOS.get("userId") == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if TODO.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(TODO.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for i in TASK_TITLE:
        print("\t {}".format(TASK))


