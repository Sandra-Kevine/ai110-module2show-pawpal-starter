# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
My initial UML design includes four classes: Owner, Pet, Task, and Scheduler. The Owner class represents the pet’s caregiver and holds their available time per day and a list of pets they manage. The Pet class stores basic info (name, species, age) and a list of care tasks. The Task class represents a single care item like feeding or a vet visit, with a due time, priority level, and completion status. The Scheduler class is responsible for looking across all tasks and figuring out what to prioritize, detect conflicts, and generate a daily plan based on the owner’s available time. The core actions a user needs are: (1) adding a pet along with its recurring care needs like feeding, walks, and medication schedules; (2) viewing a prioritized list of today’s tasks based on available time and urgency; and (3) marking tasks complete or being alerted to scheduling conflicts and overdue items.
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
My design didn’t change much from the initial UML draft — the four-class structure (Owner, Pet, Task, Scheduler) still matches what I implemented in pawpal_system.py. One small refinement was deciding to use Python dataclasses for Owner, Pet, and Task to reduce boilerplate code, while keeping Scheduler as a regular class since it manages logic across multiple objects rather than representing a single data record.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
The scheduler combines tasks from all pets owned by one Owner. It can sort by due time (using priority and task name to break ties), sort by priority, filter by pet name or completion status, and flag tasks with an identical due time. The owner model stores available minutes per day, but the current scheduling logic does not enforce that limit. Tasks also have no duration or calendar date, so the app cannot calculate time-budgeted plans, overlapping durations, or a true next-day date for recurring tasks. I focused first on behaviors that could be represented and verified with the current task fields.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
Conflict detection checks for exact matches on `due_time`, rather than overlapping time ranges. This is straightforward to implement and test, but it misses near-conflicts because tasks do not currently have duration values. It is a reasonable first version for identifying two care tasks scheduled at the same time; adding duration and date information would allow more complete conflict detection.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used my AI coding assistant to help implement the Owner, Pet, Task, and Scheduler classes, create a demo script (`main.py`), and draft and debug pytest tests. The most helpful prompts were specific to the existing code, especially asking how Scheduler should retrieve tasks from all of an Owner's pets. That led to using `Owner.get_all_tasks()` as the shared source for scheduler operations.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
I made sure Scheduler retrieves tasks through `Owner.get_all_tasks()` instead of working with a single pet. This lets it combine tasks across multiple pets. I checked the CLI output for tasks from both pets and a same-time conflict, then ran the test suite. Those checks helped verify the behavior rather than relying only on generated code.

The most useful AI features were code suggestions for implementing the class methods, help diagnosing the malformed test indentation, and assistance checking that the demo exercised multi-pet scheduling. I treated suggestions as drafts and used the tests and CLI output to verify them. I did not use a separate chat session for every phase; keeping each request focused on a specific task (design, implementation, or testing) helped me avoid mixing requirements.

This experience taught me that being the lead architect means deciding what behavior the system should support, checking that the classes work together, and verifying AI-generated changes instead of accepting them automatically.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
The five tests verify that marking a task changes its completion state, adding a task increases a pet's task count, scheduling sorts tasks chronologically, completing a recurring task adds a new incomplete occurrence to its pet, and duplicate due times are reported as conflicts. These checks cover basic task lifecycle and key scheduler behaviors. The recurrence test verifies creation of another occurrence, but the model has no date field, so it does not verify a calendar date for the following day.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am moderately confident (3 out of 5 stars) in the behaviors covered by the tests. The suite is small and does not yet verify invalid time input, an owner with no pets or tasks, equal-time tie ordering, whether completed tasks should appear in every schedule, or date-aware daily and weekly recurrence. I would test those cases next, along with duration overlap and the owner's daily time limit once those fields affect scheduling.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied that the scheduler gets tasks through the Owner and combines tasks from multiple pets. The CLI demo and tests made the behavior visible and easier to check.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would add task duration and calendar date fields, validate due-time input, and make the scheduler use the owner's available time when generating a plan. I would also make recurring tasks calculate their next date and expand the tests to cover these constraints.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
I learned that clear class responsibilities and context engineering matter: giving the AI the existing structure and a specific goal produced more useful suggestions. I still needed to review those suggestions, preserve the Owner-to-Scheduler relationship, and run tests to verify the result.
