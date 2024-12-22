import os
import json
from typing import List

TASK_FILE = r'task_detail.json'


def read_task_file()->List[dict]:
    if not os.path.isfile(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, 'r') as task_file:
            return json.load(task_file)
    except json.JSONDecodeError:
        print("Error: Task file got corrupted")
        user_input = input("Do you want to delete and proceed (yes/no)?").strip()
        if user_input.capitalize() == "Yes":
            os.remove(TASK_FILE)
            print("Corrupt file deleted, proceeding with empty file")
            return []
        else:
            print("Please delete corrupt file manually")
            exit(1)

def write_task_file(task_data:List[dict]):
    with open(TASK_FILE, 'w') as task_file:
        json.dump(task_data, task_file)
