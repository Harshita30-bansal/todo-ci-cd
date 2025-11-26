# app.py
# To-Do CLI Application

tasks = []  # each task is a dict: {"title": str, "done": bool}


def add_task(title: str) -> str:
    """Add a new task to the list."""
    title = title.strip()
    if not title:
        return "Task cannot be empty."
    tasks.append({"title": title, "done": False})
    return f"Added task: {title}"


def list_tasks() -> str:
    """Return a formatted list of tasks."""
    if not tasks:
        return "No tasks yet."
    lines = ["Your tasks:"]
    for i, t in enumerate(tasks, start=1):
        status = "x" if t["done"] else " "
        lines.append(f"{i}. [{status}] {t['title']}")
    return "\n".join(lines)


def mark_done(index: int) -> str:
    """Mark a task as completed."""
    if index < 1 or index > len(tasks):
        return "Invalid task number."
    tasks[index - 1]["done"] = True
    return f"Marked as done: {tasks[index - 1]['title']}"


def delete_task(index: int) -> str:
    """Delete a task from the list."""
    if index < 1 or index > len(tasks):
        return "Invalid task number."
    removed = tasks.pop(index - 1)
    return f"Deleted task: {removed['title']}"


def main():
    print("Welcome to To-Do CLI (IMT2023035)")
    while True:
        print("\nChoose an option:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter task: ")
            print(add_task(title))
        elif choice == "2":
            print(list_tasks())
        elif choice == "3":
            num = int(input("Enter task number to mark done: "))
            print(mark_done(num))
        elif choice == "4":
            num = int(input("Enter task number to delete: "))
            print(delete_task(num))
        elif choice == "5":
            print("Goodbye from IMT2023035!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
# app.py
# To-Do CLI Application for roll no IMT2023035

tasks = []  # each task is a dict: {"title": str, "done": bool}


def add_task(title: str) -> str:
    """Add a new task to the list."""
    title = title.strip()
    if not title:
        return "Task cannot be empty."
    tasks.append({"title": title, "done": False})
    return f"Added task: {title}"


def list_tasks() -> str:
    """Return a formatted list of tasks."""
    if not tasks:
        return "No tasks yet."
    lines = ["Your tasks:"]
    for i, t in enumerate(tasks, start=1):
        status = "x" if t["done"] else " "
        lines.append(f"{i}. [{status}] {t['title']}")
    return "\n".join(lines)


def mark_done(index: int) -> str:
    """Mark a task as completed."""
    if index < 1 or index > len(tasks):
        return "Invalid task number."
    tasks[index - 1]["done"] = True
    return f"Marked as done: {tasks[index - 1]['title']}"


def delete_task(index: int) -> str:
    """Delete a task from the list."""
    if index < 1 or index > len(tasks):
        return "Invalid task number."
    removed = tasks.pop(index - 1)
    return f"Deleted task: {removed['title']}"


def main():
    print("Welcome to To-Do CLI (IMT2023035)")
    while True:
        print("\nChoose an option:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter task: ")
            print(add_task(title))
        elif choice == "2":
            print(list_tasks())
        elif choice == "3":
            num = int(input("Enter task number to mark done: "))
            print(mark_done(num))
        elif choice == "4":
            num = int(input("Enter task number to delete: "))
            print(delete_task(num))
        elif choice == "5":
            print("Goodbye from IMT2023035!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
