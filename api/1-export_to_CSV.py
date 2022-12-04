#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format
"""
import csv
import requests
from sys



if __name__ == "__main__":

    url = requests.get("http://jsonplaceholder.typicode.com/users")
    TODO = requests.get("http://jsonplaceholder.typicode.com/todos")
    Data = url.json()
    Data2 = TODO.json()
    for users in Data:
        if users.get("id") == int(argv[1]):
            EMPLOYEE_NAME = (users["name"])
    with open(argv[1] + ".csv", "w", encoding="utf-8", newline="") as f:
        W = csv.writer(f, quoting=csv.QUOTE_ALL)
        for TODOS in Data2:
            TAB = []
            if TODOS["userId"] == int(argv[1]):
                TAB.append(TODOS["userID"])
                TAB.append(EMPLOYEE_NAME)
                TAB.append(TODOS["completed"])
                TAB.append(TODOS["title"])
                W.writerow(TAB)
