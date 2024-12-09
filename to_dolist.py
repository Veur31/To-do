import os

class Todo:
    def __init__(self):
        self.task = []
    def load_task(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename,"r") as file:
            task = file.readlines()
        return [task.strip() for task in task]
    
    def save_task(self, filename):
        with open(filename, "w") as file:
            for task in self.task:
                file.write(f"{task}\n")
    def add_task(self,task):
        self.task.append(task)
    def view_task(self):
        if not self.task:
            print("There is no task available for the moment")
        else:
            print("This is your tasks")
            for index, task in enumerate(self.task, 1):
                print(f"{index}: {task}")
    def delete_task(self, task):
        if task in self.task:
            self.task.remove(task)
            print(f"This task ({task}) has been removed")
        else:
            print("This task ({task}) is not listed")
    def line(self):
        print("-" * 50)

    def clear(self):
     choice = input("Go back to main menu? (Y/N): ").upper()
     if choice == 'Y':
          os.system('cls')
          main()
     else:
          os.system('cls')

def main():
    print("Welcome to to To-Do list.")
    todo = Todo()
    filename = "task.txt"
    todo.task= todo.load_task(filename)
    while True:
        print()
        print("Options\n1. Add task\n2. View Task\n3. Delete task\n4. Exit")
        print()
        try:
            choice = int(input("What do you wan to do? "))
            if choice == 1:
                todo.line()
                task = input("Add a task\n\nInput: ")
                todo.add_task(task)
                print("The task has been added")
                todo.line()
                todo.clear()
            elif choice == 2:
                todo.line()
                todo.view_task()
                todo.line()
                todo.clear()
            elif choice == 3:
                todo.line()
                task = input("Delete task\n\nEnter the task to be deleted: ")
                todo.delete_task(task)
                print("The task has been successfully deleted")
                todo.line()
                todo.clear
            elif choice == 4:
                todo.line()
                todo.save_task(filename)
                exit()
            else:
                print("Invalid choice")
        except ValueError:
            print("Please input a valid number")
            
main()

        