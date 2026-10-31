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
        pass

    def is_overdue(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_upcoming_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    available_time_per_day: int
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def get_today_schedule(self):
        pass


class Scheduler:
    def __init__(self, all_tasks: List[Task] = None, owner_time_available: int = 0):
        self.all_tasks = all_tasks or []
        self.owner_time_available = owner_time_available

    def prioritize_tasks(self):
        pass

    def detect_conflicts(self):
        pass

    def generate_daily_plan(self):
        pass