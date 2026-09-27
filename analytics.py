def generate_summary(tasks):
    total = len(tasks)
    if total == 0:
        print("\nNo data available to calculate statistics.")
        return

    completed = sum(1 for t in tasks if t["status"] == "COMPLETED")
    missed = sum(1 for t in tasks if t["status"] == "MISSED")
    pending = sum(1 for t in tasks if t["status"] in ["PENDING", "IN_PROGRESS"])

    score = (completed / total) * 100

    print("\n--- DAILY ADHERENCE REPORT ---")
    print(f"Total Scheduled Tasks : {total}")
    print(f"Completed Tasks       : {completed}")
    print(f"Missed Tasks          : {missed}")
    print(f"Pending/Active Tasks  : {pending}")
    print(f"Completion Score      : {score:.1f}%")
    print("------------------------------")