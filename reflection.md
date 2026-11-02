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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
My conflict detection only checks for exact matches on due_time (e.g., two tasks both at ‘08:00’), rather than detecting overlapping time ranges (e.g., a 15-minute task from 08:00-08:15 overlapping with another task starting at 08:10). This is simpler to implement and understand, but it means two tasks with slightly different times that still practically conflict (like back-to-back tasks with no buffer) won’t be flagged. I chose this tradeoff because exact-time matching covers the most common real-world case (two tasks scheduled for the identical time) and keeps the logic easy to verify, at the cost of missing near-conflicts.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
used my AI coding assistant to help implement the core logic for the Owner, Pet, Task, and Scheduler classes, generate a demo script (main.py) to verify the classes worked together correctly, and draft the pytest tests for mark_complete() and task addition. The most helpful prompts were ones where I described my existing skeleton code and asked specifically how the Scheduler should retrieve tasks from the Owner across multiple pets, since that drove a key design decision in my Scheduler class.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
One moment where I adjusted an AI suggestion was with the Scheduler class — rather than accepting it as a standalone class with no connection to Owner, I made sure it read tasks through Owner.get_all_tasks() so it would correctly combine tasks across multiple pets instead of just one. I verified this worked by running main.py and confirming the printed schedule correctly combined and sorted tasks from both pets by time, and correctly flagged a conflict between two tasks scheduled at the same time. I also ran python3 -m pytest and confirmed both tests passed, which gave me confidence the core logic (marking tasks complete and adding tasks to a pet) was working as intended.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
