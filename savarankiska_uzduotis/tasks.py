import datetime

tasks = [
{
    "taskname" : "jopapa",
    "enddate" : "2023-12-19",
},
{
    "taskname" : "example example 2",
    "enddate" : "2013-01-01"
}
    ]


def display_all_tasks(display_id=False,task_list=tasks):
    if task_list:
        if display_id:
            print("task id -", end=" ")

        print("Task name - task end date")
        for index,task in enumerate(task_list):
            print(f"{ str(index + 1)+'.' if display_id else '' } {task['taskname']} - {task['enddate']}")
    else:
        print("there are no tasks")
    return len(tasks)


def get_task_info():
    task_name = input("Please enter task name: ")
    while True:
        end_date = input("Please enter task end date(example: 2012-10-11): ")
        try:
            end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
        except ValueError:
            print("Date format is invalid!!! Please try again ")
        else:
            break

    #task = {"taskname": task_name, "enddate": end_date.strftime("%Y-%m-%d")}
    task = {"taskname": task_name, "enddate": end_date}

    return task


def add_new_task():
    task = get_task_info()
    tasks.append(task)


def get_valid_task_id(input_message=""):

    try:
        task_id = int(input(str(input_message).capitalize())) - 1
    except ValueError:
        task_id = -1

    if len(tasks) - 1 >= task_id and task_id >= 0:
        valid_id = task_id
    else:
        valid_id = -1

    return valid_id


def delete_task():
    if not display_all_tasks(display_id=True):
        return

    task_id = get_valid_task_id("Please enter task id: ")

    if task_id > -1:
        removed_task = tasks.pop(task_id)
        print(f"You have successfully deleted selected task ({removed_task['taskname']})")
    else:
        print("such task doesnt exist or already deleted")


def update_task():
    if not display_all_tasks(display_id=True):
        return

    task_id = get_valid_task_id("Please enter task id you want to update: ")

    if task_id > -1:
        task = get_task_info()
        tasks[task_id] = task
    else:
        print("such task doesnt exist")


def search_task():
    if not tasks:
        print("there are no tasks")
        return
    search_text = input("Please enter search text: ")
    search_task_list = []
    for task_id,task in enumerate(tasks):
        if task["taskname"].find(search_text) != -1 or task["enddate"].find(search_text) != -1:
            search_task_list.append(task)
    if search_task_list:
        display_all_tasks(task_list=search_task_list)
    else:
        print(f"no tasks was found by your search value : {search_text}")


def display_menu():
    while True:
        print("\n")
        print("1. Display tasks")
        print("2. Add new task")
        print("3. Delete task")
        print("4. Update task")
        print("5. Search task")
        print("0. Exit program")
        print("\n")
        try:
            command = int(input("please enter action number: "))
            print("\n")
        except ValueError:
            print("Please enter valid command")
            command = 9
        if command == 1:
            display_all_tasks()
        elif command == 2:
            add_new_task()
        elif command == 3:
            delete_task()
        elif command == 4:
            update_task()
        elif command == 5:
            search_task()
        elif command == 0:
            break
        elif command == 9:
            continue


display_menu()






