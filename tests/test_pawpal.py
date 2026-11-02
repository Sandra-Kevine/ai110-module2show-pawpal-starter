import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete_changes_status():
    task = Task(task_type="Feeding", due_time="08:00", priority=1)
    assert task.is_complete == False
    task.mark_complete()
    assert task.is_complete == True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Rex", species="Dog", age=3)
    assert len(pet.tasks) == 0
    pet.add_task(Task(task_type="Walk", due_time="17:00", priority=2))
    assert len(pet.tasks) == 1


def test_sort_by_time_returns_chronological_order():
    owner = Owner(name="Test Owner", available_time_per_day=120)
    pet = Pet(name="Buddy", species="Dog", age=2)
    pet.add_task(Task(task_type="Walk", due_time="17:00", priority=2))
    pet.add_task(Task(task_type="Feeding", due_time="08:00", priority=1))
    owner.add_pet(pet)
    scheduler = Scheduler(owner=owner)

    sorted_tasks = scheduler.sort_by_time()
    assert sorted_tasks[0].due_time == "08:00"
    assert sorted_tasks[1].due_time == "17:00"


def test_recurring_task_creates_next_occurrence():
    owner = Owner(name="Test Owner", available_time_per_day=120)
    pet = Pet(name="Buddy", species="Dog", age=2)
    recurring_task = Task(task_type="Medicine", due_time="09:00", priority=1, is_recurring=True, frequency="daily")
    pet.add_task(recurring_task)
    owner.add_pet(pet)
    scheduler = Scheduler(owner=owner)

    next_task = scheduler.complete_task(recurring_task)
    assert recurring_task.is_complete == True
    assert next_task is not None
    assert next_task.task_type == "Medicine"
    assert next_task in pet.tasks


def test_detect_conflicts_flags_same_time_tasks():
    owner = Owner(name="Test Owner", available_time_per_day=120)
    pet1 = Pet(name="Buddy", species="Dog", age=2)
    pet2 = Pet(name="Whiskers", species="Cat", age=1)
    pet1.add_task(Task(task_type="Feeding", due_time="08:00", priority=1))
    pet2.add_task(Task(task_type="Feeding", due_time="08:00", priority=1))
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    scheduler = Scheduler(owner=owner)

    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1