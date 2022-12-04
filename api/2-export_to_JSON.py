#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = requests.get("http://jsonplaceholder.typicode.com/users")
    TODO = requests.get("http://jsonplaceholder.typicode.com/todos")
    Data = url.json()
    Data2 = TODO.json()
    tab = []

    for users in Data:
        if users.get("id") == int(argv[1]):
            EMPLOYEE_uNAME = (users["username"])
            ID = (users["id"])

    for TODOS in Data2:
        TAB = {}
        if TODOS["userId"] == int(argv[1]):
            TAB["username"] = EMPLOYEE_uNAME
            TAB["task"] = TODOS["title"]
            TAB["completed"] = TODOS["completed"]
            tab.append(TAB)

    dict_f = {}
    dict_f[ID] = tab
    json_f = json.dumps(dict_f)

    with open(argv[1] + ".json", "w", encoding="utf-8") as f:
        f.write(json_f)
