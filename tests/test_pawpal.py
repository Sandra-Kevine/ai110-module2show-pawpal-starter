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