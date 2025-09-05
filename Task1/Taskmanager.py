import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)
            for task in self.tasks:
                if "created" not in task:
                    task["created"] = "Unknown"

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add(self, task):
        self.tasks.append({
            "task": task,
            "done": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save()

    def complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save()

    def remove(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()

    def show(self):
        for i, t in enumerate(self.tasks):
            status = "✓" if t["done"] else "✗"
            created = t.get("created", "Unknown")
            print(f"{i + 1}. [{status}] {t['task']} (Added: {created})")

manager = TaskManager("tasks.json")

while True:
    print("\n1. Add Task\n2. Complete Task\n3. Remove Task\n4. Show Tasks\n5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        task = input("Enter task: ")
        manager.add(task)
    elif choice == "2":
        index = int(input("Enter task number to complete: ")) - 1
        manager.complete(index)
    elif choice == "3":
        index = int(input("Enter task number to remove: ")) - 1
        manager.remove(index)
    elif choice == "4":
        manager.show()
    elif choice == "5":
        break
