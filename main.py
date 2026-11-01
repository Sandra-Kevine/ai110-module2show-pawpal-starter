from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner
owner = Owner(name="Sandra", available_time_per_day=120)

# Create two pets
dog = Pet(name="Rex", species="Dog", age=3)
cat = Pet(name="Whiskers", species="Cat", age=2)

# Add tasks to each pet
dog.add_task(Task(task_type="Feeding", due_time="08:00", priority=1))
dog.add_task(Task(task_type="Walk", due_time="17:00", priority=2))
cat.add_task(Task(task_type="Feeding", due_time="08:00", priority=1))

# Add pets to the owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create a scheduler linked to the owner
scheduler = Scheduler(owner=owner)

# Print today's schedule
print("=== Today's Schedule ===")
for task in scheduler.generate_daily_plan():
    print(f"{task.due_time} - {task.task_type} (priority {task.priority})")

# Check for conflicts
print("\n=== Conflict Check ===")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for t1, t2 in conflicts:
        print(f"Conflict: {t1.task_type} and {t2.task_type} both at {t1.due_time}")

    print("No conflicts found.")
    print("\n=== Sorted by Time ===")
for task in scheduler.sort_by_time():
    print(f"{task.due_time} - {task.task_type}")

print("\n=== Filter: Incomplete tasks only ===")
for task in scheduler.filter_tasks(is_complete=False):
    print(f"{task.due_time} - {task.task_type}")