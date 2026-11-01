import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
# Keep the Owner object alive across reruns using session_state
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name, available_time_per_day=120)



owner = st.session_state.owner
owner.name = owner_name

# Find the pet by name, or create a new one if it doesn't exist yet
pet = next((p for p in owner.pets if p.name == pet_name), None)
if pet is None:
    pet = Pet(name=pet_name, species=species, age=0)
    owner.add_pet(pet)

st.markdown("### Tasks")
st.caption("Add a few tasks. These feed directly into your Scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    due_time = st.text_input("Due time (HH:MM)", value="08:00")
with col3:
    priority_label = st.selectbox("Priority", ["low", "medium", "high"], index=2)

priority_map = {"high": 1, "medium": 2, "low": 3}

if st.button("Add task"):
    new_task = Task(
        task_type=task_title,
        due_time=due_time,
        priority=priority_map[priority_label],
    )
    pet.add_task(new_task)
    st.success(f"Added '{task_title}' at {due_time} for {pet.name}")

if pet.tasks:
    st.write("Current tasks:")
    st.table([
        {"Task": t.task_type, "Time": t.due_time, "Priority": t.priority, "Done": t.is_complete}
        for t in pet.tasks
    ])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

st.caption("This calls your Scheduler to generate today's plan and check for conflicts.")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner=owner)
    plan = scheduler.generate_daily_plan()
    conflicts = scheduler.detect_conflicts()

    if plan:
        st.success("Today's Schedule:")
        st.table([
            {"Time": t.due_time, "Task": t.task_type, "Priority": t.priority}
            for t in plan
        ])
    else:
        st.info("No tasks scheduled yet. Add tasks above first.")

    if conflicts:
        for t1, t2 in conflicts:
            st.warning(f"Conflict: {t1.task_type} and {t2.task_type} both at {t1.due_time}")