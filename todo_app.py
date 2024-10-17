#Step 1: Displaying a Menu
def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark as done")
    print("4.Exit")

#step 2: Adding Tasks
def add_task(tasks):
    task=input("Enter your task:")
    tasks.append(task)
    print("Task sucssfully added")

#step 3: Viewing Tasks
def view_task(tasks):
    print("/nTasks:")
    for i,  task in enumerate (tasks, start=1):
      print(f"{i}. {task}") 
    #   print(format(i.tasks)) 
      print('index num  is {0} and task is {1}'.format(i,task))
      
#Step 4: Marking Tasks as Done
def mark_done(tasks):
    if not tasks:
        print("task is not available")


    view_task(tasks) #display list of task with indices
    index = int(input("Enter task index to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        return f"Task '{removed_task}' marked as done and removed."
    else:
        return "Invalid task index."
        
#step 5: Main logic
def main():
    tasks = []  # Initialize an empty list to store tasks
    
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()