# test_app.py
from app import add_task, list_tasks, mark_done, delete_task, tasks


def setup_function():
    # runs before each test – clear the list
    tasks.clear()


def test_add_task():
    msg = add_task("Finish SE lab")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Finish SE lab"
    assert msg == "Added task: Finish SE lab"


def test_add_empty_task():
    msg = add_task("   ")
    assert len(tasks) == 0
    assert msg == "Task cannot be empty."


def test_list_empty():
    result = list_tasks()
    assert result == "No tasks yet."


def test_list_non_empty():
    add_task("Task 1")
    add_task("Task 2")
    result = list_tasks()
    assert "1. [ ] Task 1" in result
    assert "2. [ ] Task 2" in result


def test_mark_done_valid():
    add_task("Task 1")
    msg = mark_done(1)
    assert tasks[0]["done"] is True
    assert msg == "Marked as done: Task 1"


def test_mark_done_invalid():
    msg = mark_done(5)
    assert msg == "Invalid task number."


def test_delete_task_valid():
    add_task("Task 1")
    add_task("Task 2")
    msg = delete_task(1)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task 2"
    assert msg == "Deleted task: Task 1"


def test_delete_task_invalid():
    add_task("Task 1")
    msg = delete_task(3)
    assert len(tasks) == 1
    assert msg == "Invalid task number."
