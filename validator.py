from datetime import datetime

def parse_time(time_str):
    try:
        return datetime.strptime(time_str.strip(), "%H:%M")
    except ValueError:
        return None

def check_overlap(start_str, end_str, existing_tasks, ignore_id=None):
    new_start = parse_time(start_str)
    new_end = parse_time(end_str)

    if not new_start or not new_end:
        return "Invalid format. Please use HH:MM (24-hour time)."
    
    if new_start >= new_end:
        return "Start time must be before end time."

    for task in existing_tasks:
        if ignore_id and task["id"] == ignore_id:
            continue
        
        task_start = parse_time(task["start"])
        task_end = parse_time(task["end"])
        
        if new_start < task_end and task_start < new_end:
            return f"Time conflict with '{task['title']}' ({task['start']} - {task['end']})."

    return None