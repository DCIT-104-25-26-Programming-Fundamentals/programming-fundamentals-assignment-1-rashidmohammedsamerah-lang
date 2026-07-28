def add_task(tasks):
    task = input("Enter task: ")

    tasks.append(task)

    print(f'Task added: "{task}"')


def view_tasks(tasks):
    if len(tasks) == 0:
        print("Your task list is empty.")
    else:
        print("\nYour Tasks:")

        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)

    number = int(input("Enter task number to delete: "))

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
    else:
        removed_task = tasks.pop(number - 1)

        print(f'Task "{removed_task}" has been removed.')


def display_menu():
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


# Main Program

tasks = []

while True:
    display_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")