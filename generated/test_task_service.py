import pytest

from generated.task_service import TaskService


def test_create_task():
    service = TaskService()

    task = service.create_task(
        title="Study Python",
        description="Practice classes and functions",
        priority="high",
    )

    assert task.id == 1
    assert task.title == "Study Python"
    assert task.completed is False


def test_list_tasks():
    service = TaskService()
    service.create_task("Task 1", "First task", "low")
    service.create_task("Task 2", "Second task", "medium")

    tasks = service.list_tasks()

    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_complete_task():
    service = TaskService()
    task = service.create_task("Finish report", "Write the final report", "medium")

    completed_task = service.complete_task(task.id)

    assert completed_task.completed is True
    assert completed_task.completed_at is not None


def test_delete_task():
    service = TaskService()
    task = service.create_task("Delete me", "Temporary task", "low")

    service.delete_task(task.id)

    tasks = service.list_tasks()
    assert len(tasks) == 0


def test_invalid_priority():
    service = TaskService()

    with pytest.raises(ValueError, match="Priority must be: low, medium, or high."):
        service.create_task(
            title="Bad priority",
            description="This should fail",
            priority="urgent",
        )
