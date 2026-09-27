GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_header(title):
    print("\n" + "=" * 50)
    print(f"   {title}")
    print("=" * 50)

def render_schedule(tasks):
    if not tasks:
        print("\nNo routine tasks added yet.")
        return

    print_header("DAILY ROUTINE TIMETABLE")
    print(f"{'ID':<4} {'TIME SLOT':<15} {'TASK TITLE':<20} {'STATUS'}")
    print("-" * 50)

    sorted_tasks = sorted(tasks, key=lambda x: x["start"])

    for t in sorted_tasks:
        status = t["status"]
        if status == "COMPLETED":
            status_text = f"{GREEN}[COMPLETED]{RESET}"
        elif status == "MISSED":
            status_text = f"{RED}[MISSED]{RESET}"
        elif status == "IN_PROGRESS":
            status_text = f"{YELLOW}[IN PROGRESS]{RESET}"
        else:
            status_text = "[PENDING]"

        time_slot = f"{t['start']} - {t['end']}"
        print(f"{t['id']:<4} {time_slot:<15} {t['title']:<20} {status_text}")
    print("-" * 50)