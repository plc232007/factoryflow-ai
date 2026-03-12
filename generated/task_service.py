from datetime import datetime
    from typing import List

    from generated.task import Task


    class TaskService:
        def __init__(self):
            self.tasks: List[Task] = []
            self.next_id = 1

        def create_task(self, title: str, description: str, priority: str) -> Task:
            if not title.strip():
                raise ValueError("Title is required.")

            valid_priorities = {"low", "medium", "high"}
            if priority not in valid_priorities:
                raise ValueError("Priority must be: low, medium, or high.")

            task = Task(
                id=self.next_id,
                title=title,
                description=description,
                priority=priority,
            )
            self.tasks.append(task)
            self.next_id += 1
            return task

        def list_tasks(self) -> List[Task]:
            return self.tasks

        def complete_task(self, task_id: int) -> Task:
            task = self._find_task(task_id)
            task.completed = True
            task.completed_at = datetime.utcnow()
            return task

        def delete_task(self, task_id: int) -> None:
            task = self._find_task(task_id)
            self.tasks.remove(task)

        def _find_task(self, task_id: int) -> Task:
            for task in self.tasks:
                if task.id == task_id:
                    return task
            raise ValueError(f"Task with id {task_id} not found.")
