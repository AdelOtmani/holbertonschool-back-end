#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format
"""
import requests
from requests import get
from sys import argv
import csv


if __name__ == "__main__":

    url = requests.get("http://jsonplaceholder.typicode.com/users")
    TODO = requests.get("http://jsonplaceholder.typicode.com/todos")
    Data = url.json()
    Data2 = TODO.json()
    TAB = []
    for users in Data:
        if users.get("id") == int(argv[1]):
            EMPLOYEE_NAME = (users.get("name"))
    with open(argv[1] + ".csv", "w", encoding="utf-8", newline="") as f:
        W = csv.writer(f, quoting=csv.QUOTE_ALL)
        for TODOS in Data2:
            if TODOS.get("userId") == int(argv[1]):
                TAB.append(TODOS.get("userID"))
                TAB.append(EMPLOYEE_NAME)
                TAB.append(TODOS.get("completed"))
                TAB.append(TODOS.get("title"))
                W.writerow(TAB)