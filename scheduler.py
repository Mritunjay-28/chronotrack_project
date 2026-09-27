from datetime import datetime
from validator import parse_time
from notifier import trigger_alert
from storage import save_data

def check_routine_status(tasks):
    now_dt = datetime.now()
    current_time = parse_time(now_dt.strftime("%H:%M"))
    updated = False

    for t in tasks:
        start_dt = parse_time(t["start"])
        end_dt = parse_time(t["end"])

        if start_dt <= current_time < end_dt:
            if t["status"] == "PENDING":
                t["status"] = "IN_PROGRESS"
                trigger_alert(t["title"], "START")
                updated = True

        elif current_time >= end_dt:
            if t["status"] in ["PENDING", "IN_PROGRESS"]:
                trigger_alert(t["title"], "END")
                print(f"\nDid you complete '{t['title']}' ({t['start']} - {t['end']})?")
                answer = input("Enter 'y' for Completed, 'n' for Missed: ").strip().lower()
                
                if answer == "y":
                    t["status"] = "COMPLETED"
                else:
                    t["status"] = "MISSED"
                updated = True

    if updated:
        save_data(tasks)