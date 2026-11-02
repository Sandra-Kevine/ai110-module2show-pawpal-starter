# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Features

The project includes a Python scheduling backend and a basic Streamlit demo:

The system is built around four classes — Owner, Pet, Task, and Scheduler. An Owner manages multiple Pets, each of which holds a list of Tasks. The Scheduler reads tasks across all of an owner's pets (via Owner.get_all_tasks()) to generate a prioritized daily plan and detect scheduling conflicts.

- **Sorting:** `Scheduler.generate_daily_plan()` and `Scheduler.sort_by_time()` order tasks by time, then priority and task name.
- **Priority ordering:** `Scheduler.prioritize_tasks()` places lower-numbered priorities first.
- **Filtering:** `Scheduler.filter_tasks()` filters by pet name and/or completion state.
- **Conflict warnings:** `Scheduler.detect_conflicts()` reports pairs of tasks with exactly matching due times.
- **Recurring task handling:** completing a recurring task creates another incomplete task with the same time and frequency. The current model does not store calendar dates, so it does not calculate a distinct next-day or next-week date.
- **Streamlit demo:** add a pet-care task, view the pet's tasks, generate a schedule, and see exact-time conflict warnings.

The owner’s available time is stored but is not yet used to limit the generated schedule. Tasks also do not currently have duration fields, so the scheduler does not detect overlapping time ranges.

## Getting Started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🧪 Testing PawPal+

```bash
python -m pytest
```

The tests cover task completion, adding a task to a pet, chronological sorting, recurring-task creation, and duplicate-time conflict detection. The current test run passed all five tests:

```text
============================= test session starts ==============================
platform darwin -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: .
plugins: anyio-4.15.1
collected 5 items

tests/test_pawpal.py .....                                               [100%]

============================== 5 passed in 0.01s ===============================
```

**Confidence level: 3/5 stars.** The five tests verify important core behaviors, but calendar-aware recurrence, task durations, available-time limits, and invalid-time input still need tests and implementation.

## 🖥️ Demo Walkthrough

1. Run `streamlit run app.py` to open the interactive demo.
2. Enter an owner name and pet name, choose a species, then enter a task title, due time, and priority.
3. Select **Add task** to add it to the selected pet. The current task list shows each task's time, priority, and completion state.
4. Select **Generate schedule** to display the owner's tasks ordered by time. Tasks with the same due time are shown as conflict warnings.
5. To see the backend example in a terminal, run `python main.py`. It creates an owner with two pets, prints the combined schedule, demonstrates conflict detection and filtering, and completes a recurring task.

Sample CLI output from `python main.py`:

```text
=== Today's Schedule ===
08:00 - Feeding (priority 1)
08:00 - Feeding (priority 1)
17:00 - Walk (priority 2)

=== Conflict Check ===
Conflict: Feeding and Feeding both at 08:00

=== Sorted by Time ===
08:00 - Feeding
08:00 - Feeding
17:00 - Walk

=== Filter: Incomplete tasks only ===
08:00 - Feeding
17:00 - Walk
08:00 - Feeding

=== Testing Recurring Task ===
Completed: Give medicine, is_complete=True
Next occurrence created: Give medicine at 09:00
```
