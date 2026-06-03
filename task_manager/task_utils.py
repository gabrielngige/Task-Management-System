from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []


def add_task(title, description, due_date):
    validated_title = validate_task_title(title)
    validated_description = validate_task_description(description)
    validated_due_date = validate_due_date(due_date)

    task = {
        "title": validated_title,
        "description": validated_description,
        "due_date": validated_due_date,
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return
    if index < 1 or index > len(tasks):
        print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
        return
    task = tasks[index - 1]
    if task["completed"]:
        print(f"Task '{task['title']}' is already marked as complete.")
    else:
        task["completed"] = True
        print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return
    print("\nPending Tasks:")
    print("-" * 40)
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"  Task #{i + 1}")
            print(f"  Title      : {task['title']}")
            print(f"  Description: {task['description']}")
            print(f"  Due Date   : {task['due_date']}")
            print()


def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed_count = sum(1 for t in tasks if t["completed"])
    progress = (completed_count / len(tasks)) * 100
    return progress
