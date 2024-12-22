import argparse
from commands import command

msg = "Task tracker CLI application"
parser = argparse.ArgumentParser(description=msg,add_help=True)
subparser = parser.add_subparsers(dest="command", help="Sub commands")


# creating parser for list cmd
list_parser = subparser.add_parser("list", help="List task command")
list_parser.add_argument(#"-f", "--filter",
                         dest="filter_condition",
                         choices=["all", "done", "in-progress","todo"],
                         help="Filter the task",
                         default="all")


# create parser for mark cmd
mark_parser = subparser.add_parser("mark", help="Mark task command")
mark_parser.add_argument(#"-s","--status",
                         dest="status",
                         choices=["in-progress","done"],
                         help="Choice to mark task",)
                         #required=True)
mark_parser.add_argument(# "-id",
                         dest="id",
                         help="Task id",
                         type=int,
                         nargs=1, )
                         # required=True)

# create parser for add cmd
add_parser = subparser.add_parser("add", help="add new task command")
add_parser.add_argument(# "-d", "--desc",
                        dest="description",
                        help="Description of task", type=str, nargs=1)

# create parser for update cmd
update_parser = subparser.add_parser("update", help="update task command")
update_parser.add_argument(#"-id",
                           dest="id",
                           help="Task id",
                           type=int,
                           nargs=1,)
                           # required=True)
update_parser.add_argument(#"-d", "--desc",
                           dest="description",
                           help="New description of task",
                           type= str, nargs=1,)
                           # required=True)

#create parser to delete task
delete_parser = subparser.add_parser("delete", help="Delete task command")
delete_parser.add_argument(#"-id",
                           dest="id",
                           help="Task id",
                           type=int,
                           nargs=1,)
                           # required=True)


args = parser.parse_args()
# print(args)
# print(args.command)

if args.command == "add":
    task_id = command.add_task(args.description)
    print(f"Task added successfully (ID: {task_id})")

elif args.command == "update":
    task_id = args.id
    description = args.description
    command.update_task(task_id[0], description[0])

elif args.command == "delete":
    command.delete_task(args.id[0])

elif args.command == "mark":
    task_id = args.id
    task_status = args.status
    command.mark_task(task_status, task_id[0])

elif args.command == "list":
    filter_condition = args.filter_condition
    tasks = command.list_tasks(filter_condition)
    for task in tasks:
        print(task)
