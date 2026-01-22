import json

def add_task(task):
    data.append({"task": task, "done": False})

def show_tasks():
    if not data:
        print("No tasks found")
    for i, t in enumerate(data):
        status = "Done" if t["done"] else "Pending"
        print(f"{i+1}. {t['task']} - {status}")

def mark_done(index):
    data[index]["done"] = True

try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task(input("Enter task: "))
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_done(int(input("Enter task number: ")) - 1)
    elif choice == "4":
        break

    with open("data.json", "w") as f:
        json.dump(data, f)
