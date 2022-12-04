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
    dict_f = {}

    for users in Data:
        for TODOS in Data2:
            if users.get("id") == TODOS["userId"]:
                TAB = {}
                TAB["username"] = user["username"]
                TAB["task"] = TODOS["title"]
                TAB["completed"] = TODOS["completed"]
                tab.append(TAB)
        
        dict_f[user["id"]] = tab

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json_f = json.dumps(dict_f)
        f.write(json_f)
