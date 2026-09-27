import sys

def trigger_alert(task_title, message_type):
    sys.stdout.write("\a")
    sys.stdout.flush()

    print("\n" + "*" * 40)
    if message_type == "START":
        print(f"⏰ TIME TO START: {task_title.upper()}!")
    elif message_type == "END":
        print(f"🔔 SLOT ENDED: {task_title.upper()}!")
    print("*" * 40 + "\n")