from datetime import datetime
from typing import List
from utilities import utility


def add_task(description:str)->int:
    if description:
        new_task = dict()
        tasks = utility.read_task_file()
        if tasks:
            new_task["id"] = tasks[-1]["id"] + 1
        else:
            new_task["id"] = 1
        new_task["status"] = "todo"
        new_task["description"] = description[0]
        new_task["createdAt"] = new_task["updatedAt"] = datetime.now().isoformat()
        tasks.append(new_task)
        utility.write_task_file(tasks)
        return new_task["id"]
    else:
        print("Please provide description of task")
        return 0

def update_task(task_id:int, description:str)->None:
    tasks = utility.read_task_file()
    if task_id <= 0:
        print(f"Invalid task (ID:{task_id})")
        return
    if task_id > tasks[-1]["id"]:
        print(f"Task (ID:{task_id}) does not exists")
        return
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            break
    utility.write_task_file(tasks)
    print(f"Task (ID:{task_id}) updated successfully")

def delete_task(task_id:int)->None:
    tasks = utility.read_task_file()
    if task_id <= 0:
        print(f"Invalid task (ID:{task_id})")
        return
    if task_id > tasks[-1]["id"]:
        print(f"Task (ID:{task_id}) does not exists")
        return
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            del tasks[i]
            break
    utility.write_task_file(tasks)
    print(f"Task (ID:{task_id}) deleted successfully")

def list_tasks(filter_condition:str)->List[dict]:
    tasks = utility.read_task_file()
    if filter_condition == "all":
        return tasks
    elif filter_condition == "done":
        result = []
        for task in tasks:
            if task["status"]=="done":
                result.append(task)
        return result
    elif filter_condition == "in-progress":
        result = []
        for task in tasks:
            if task["status"] == "in-progress":
                result.append(task)
        return result
    elif filter_condition == "todo":
        result = []
        for task in tasks:
            if task["status"] == "todo":
                result.append(task)
        return result

def mark_task(task_status:str, task_id:int)->None:
    tasks = utility.read_task_file()
    if task_id <= 0:
        print(f"Invalid task (ID:{task_id})")
        return
    if task_id > tasks[-1]["id"]:
        print(f"Task (ID:{task_id}) does not exists")
        return
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = task_status
            task["updatedAt"] = datetime.now().isoformat()
            break
    utility.write_task_file(tasks)
    print(f"Task (ID:{task_id}) marked successfully")