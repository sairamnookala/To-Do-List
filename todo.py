import json
from datetime import datetime

TASK_FILE = 'tasks.json'

class Task:
    def __init__(self, description, priority, due_date, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['priority'], data['due_date'], data['completed'])

def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            tasks_data = json.load(file)
            return [Task.from_dict(task) for task in tasks_data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def add_task(description, priority, due_date):
    tasks = load_tasks()
    tasks.append(Task(description, priority, due_date))
    save_tasks(tasks)

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)

def mark_task_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = 'Done' if task.completed else 'Not Done'
        print(f"{i + 1}. {task.description} | Priority: {task.priority} | Due: {task.due_date} | Status: {status}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(description, priority, due_date)
        
        elif choice == '2':
            index = int(input("Enter task number to remove: ")) - 1
            remove_task(index)
        
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(index)
        
        elif choice == '4':
            list_tasks()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
