# Task Tracker CLI
## Description
The Task Tracker CLI is a Python-based command-line tool designed to help users track their daily task. It leverages the argparse, os and json library to provide a user-friendly interface for adding, viewing, and managing task. The tool supports various features such as adding new task, update task, lsit task, mark task, delete task.

It is inspired from the Task Tracker project featured in the Backend Roadmap from roadmap.sh.

## Features
- **Add Task:** Easily add new task with it's description.
- **Delete Task:** Delete a task based on it's ID.
- **List Task:** Display a list of all the tasks as well as based on filter condition (all, todo, in-progress, done).
- **Update Task:** Update the description of task based on it's ID.
- **Mark Task:** Mark status of task (in-progress, done) based on it's ID

## Prerequisites
- Python 3.10+
- Git
  
## Installation
1. **Clone the Repository:**
``` python
git clone https://github.com/LalitSinghParmar/Task-trackerCLI.git
cd Task-trackerCLI
```
2. Create and Activate a Virtual Environment
```sh
  python -m venv venv
  # On Windows:
  .\venv\Scripts\activate

  # On macOS and Linux:
  source .venv/bin/activate
```
3. Install Dependencies
```sh
pip install -r requirements.txt
```
## Usage
-  Run the application
```sh
python task_tracker_cli -h # Show help
python task_tracker_cli add "Task 1" # Add a task
python task_tracker_cli update 1 "New description" # update new description for task with id 1 
python task_tracker_cli delete 1 # Delete task with id 1
python task_tracker_cli mark done 1 # Mark task with id 1 to done
python task_tracker_cli mark in-progress 1 # Mark task with id 1 to in-progress
python task_tracker_cli list all # list all task
python task_tracker_cli list todo # list all task having status todo
python task_tracker_cli list in-progress # list all task having status in-progress
python task_tracker_cli list done # list all task having status done
```
