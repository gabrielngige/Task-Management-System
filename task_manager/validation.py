from datetime import datetime


def validate_task_title(title):
    if not title or len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    if len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    if len(title.strip()) > 100:
        raise ValueError("Title cannot exceed 100 characters.")
    return title.strip()


def validate_task_description(description):
    if not description or len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    if len(description.strip()) < 5:
        raise ValueError("Description must be at least 5 characters long.")
    if len(description.strip()) > 500:
        raise ValueError("Description cannot exceed 500 characters.")
    return description.strip()


def validate_due_date(due_date):
    if not due_date or len(due_date.strip()) == 0:
        raise ValueError("Due date cannot be empty.")
    try:
        parsed_date = datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format (e.g. 2024-06-26).")
    if parsed_date.date() < datetime.today().date():
        raise ValueError("Due date cannot be in the past.")
    return due_date.strip()
