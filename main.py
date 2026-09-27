import sys
from storage import load_data, save_data, get_next_id
from validator import check_overlap
from display import render_schedule, print_header
from scheduler import check_routine_status
from analytics import generate_summary

def add_task(tasks):
    print_header("ADD NEW TASK")
    title = input("Task title (e.g. Gym, Study): ").strip()
    if not title:
        print("Title cannot be blank.")
        return

    start = input("Start time (HH:MM, 24-hr format): ").strip()
    end = input("End time (HH:MM, 24-hr format): ").strip()

    error = check_overlap(start, end, tasks)
    if error:
        print(f"Error: {error}")
        return

    new_task = {
        "id": get_next_id(tasks),
        "title": title,
        "start": start,
        "end": end,
        "status": "PENDING"
    }
    tasks.append(new_task)
    save_data(tasks)
    print(f"Task '{title}' scheduled successfully!")

def delete_task(tasks):
    render_schedule(tasks)
    try:
        t_id = int(input("\nEnter Task ID to delete: "))
        found = False
        for i, t in enumerate(tasks):
            if t["id"] == t_id:
                deleted = tasks.pop(i)
                save_data(tasks)
                print(f"Deleted task: {deleted['title']}")
                found = True
                break
        if not found:
            print("Task ID not found.")
    except ValueError:
        print("Please enter a valid numeric ID.")

def reset_all_status(tasks):
    confirm = input("Reset all tasks back to PENDING for a new day? (y/n): ").strip().lower()
    if confirm == "y":
        for t in tasks:
            t["status"] = "PENDING"
        save_data(tasks)
        print("All task statuses have been reset.")

def main():
    while True:
        tasks = load_data()
        check_routine_status(tasks)

        print("\n=== CHRONOTRACK MENU ===")
        print("1. View Schedule (Color Dashboard)")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Check Time Alerts / Update Status")
        print("5. View Daily Report & Analytics")
        print("6. Reset Daily Progress")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            render_schedule(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Checking active slots against current time...")
            check_routine_status(tasks)
            save_data(tasks)
            print("Check complete.")
        elif choice == "5":
            generate_summary(tasks)
        elif choice == "6":
            reset_all_status(tasks)
        elif choice == "7":
            print("Exiting ChronoTrack. Stay consistent!")
            sys.exit(0)
        else:
            print("Invalid choice, please enter 1 to 7.")

if __name__ == "__main__":
    main()