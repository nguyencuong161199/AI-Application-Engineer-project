
# Task Manager - Command Line Application

# Initialize an empty list to store tasks
tasks = []

# Add a new task to the task list
def add_task(description):
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": task_id, "description": description, "completed": False}
    tasks.append(task)
    print(f"Task '{description}' added with ID {task_id}.")

# Display all tasks with their status
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f"{task['id']}: {task['description']} [{status}]")

# Mark a task as completed using its ID
def mark_completed(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task ID {task_id} marked as completed.")
            return
    print(f"No task found with ID {task_id}.")

# Delete a task by its ID
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print(f"Task ID {task_id} deleted if it existed.")

# Main loop for user interaction
def main():
    while True:
        print("\nOptions: add, view, complete, delete, exit")
        choice = input("Enter command: ").strip().lower()
        if choice == "add":
            desc = input("Enter task description: ").strip()
            # Check if the task description is empty
            if not desc:
            # Inform the user that the input is invalid
                print("Description cannot be empty.")
                continue
            add_task(desc)
        elif choice == "view":
            view_tasks()
        elif choice == "complete":
            try:
                # Get and validate task ID input for completion
                task_id_input = input("Enter task ID to mark complete: ").strip()
                # Ensure the task ID is a number
                if not task_id_input.isdigit():
                # Inform the user if ID is invalid
                    print("Invalid task ID.")
                    continue
                task_id = int(task_id_input)
                mark_completed(task_id)
            except ValueError:
                # Inform the user if ID is invalid
                print("Invalid task ID.")
        elif choice == "delete":
            try:
                # Get and validate task ID input for deletion
                task_id_input = input("Enter task ID to delete: ").strip()
                # Ensure the task ID is a number
                if not task_id_input.isdigit():
                # Inform the user if ID is invalid
                    print("Invalid task ID.")
                    continue
                task_id = int(task_id_input)
                delete_task(task_id)
            except ValueError:
                # Inform the user if ID is invalid
                print("Invalid task ID.")
        elif choice == "exit":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
