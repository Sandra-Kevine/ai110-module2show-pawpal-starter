from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    task_type: str
    due_time: str
    priority: int
    is_recurring: bool = False
    is_complete: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.is_complete = True

    def is_overdue(self):
        """Return True if the task is not complete (simple placeholder check)."""
        return not self.is_complete


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a new task to this pet's task list."""
        self.tasks.append(task)

    def get_upcoming_tasks(self):
        """Return all tasks for this pet that are not yet complete."""
        return [task for task in self.tasks if not task.is_complete]


@dataclass
class Owner:
    name: str
    available_time_per_day: int
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a new pet to this owner's list of pets."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return every task across all of this owner's pets combined."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def get_today_schedule(self):
        """Return all tasks across all pets (today's schedule)."""
        return self.get_all_tasks()


class Scheduler:
    def __init__(self, owner: Owner = None):
        self.owner = owner

    def get_all_tasks(self):
        """Retrieve all tasks by asking the Owner, not a single pet."""
        if self.owner is None:
            return []
        return self.owner.get_all_tasks()

    def prioritize_tasks(self):
        """Return tasks sorted by priority (lower number = higher priority)."""
        return sorted(self.get_all_tasks(), key=lambda t: t.priority)

    def detect_conflicts(self):
        """Return a list of tasks that share the same due_time (placeholder)."""
        tasks = self.get_all_tasks()
        seen_times = {}
        conflicts = []
        for task in tasks:
            if task.due_time in seen_times:
                conflicts.append((seen_times[task.due_time], task))
            else:
                seen_times[task.due_time] = task
        return conflicts

    def generate_daily_plan(self):
        """Return tasks sorted by due_time to form a simple daily plan."""
        return sorted(self.get_all_tasks(), key=lambda t: t.due_time)