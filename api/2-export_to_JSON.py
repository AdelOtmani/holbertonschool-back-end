#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = requests.get("http://jsonplaceholder.typicode.com/users")
    TODO = requests.get("http://jsonplaceholder.typicode.com/todos")
    Data = url.json()
    Data2 = TODO.json()

    for users in Data:
        if users.get("id") == int(argv[1]):
            EMPLOYEE_NAME = (users["username"])
            ID = (users["id"])

        for TODOS in Data2:
            tab=[]
            TAB = {}
            if TODOS["userId"] == int(argv[1]):
                TAB["username"] = EMPLOYEE_NAME
                TAB["task"] = TODOS["title"]
                TAB["completed"] = TODOS["completed"]
                tab.append(TAB)
        
        dict_f = {}
        dict_f[ID] = tab
        json_f = json.dumb(dict_f)

    with open(argv[1] + ".csv", "w", encoding="utf-8", newline="") as f:
        f.write(json_f)
