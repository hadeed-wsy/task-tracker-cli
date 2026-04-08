import sys
import json
import time

FILE = "tasks.json"

def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def update_status(index, status):
    tasks = load()
    tasks[index - 1]["status"] = status
    save(tasks)
    print("Updated status:", status)

def add(task):
    tasks = load()
    new_id = max([t["id"] for t in tasks], default=0) + 1
    now = time.strftime("%d-%m-%Y %H:%M:%S")

    tasks.append({
        "id": new_id,
        "description": task,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    })

    save(tasks)
    print("Added:", task)

def mark(index, status):
    tasks = load()
    now = time.strftime("%d-%m-%Y %H:%M:%S")

    tasks[index - 1]["status"] = status
    tasks[index - 1]["updatedAt"] = now

    save(tasks)
    print("Status updated:", status)

def update(index, new_task):
    tasks = load()
    now = time.strftime("%d-%m-%Y %H:%M:%S")

    tasks[index - 1]["description"] = new_task
    tasks[index - 1]["updatedAt"] = now

    save(tasks)
    print("Updated:", new_task)

def delete(index):
    tasks = load()
    removed = tasks.pop(index-1)
    save (tasks)
    print("Removed:", tasks)

def list_tasks():
    tasks = load()

    for t in tasks:
        print(
            f'{t["id"]}. [{t["status"]}] {t["description"]} '
            f'(created: {t["createdAt"]}, updated: {t["updatedAt"]})'
        )

# CLI handling
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: add <task> | list")
        sys.exit()

    cmd = sys.argv[1]

    if cmd == "add":
        add(sys.argv[2])

    elif cmd == "list":
        list_tasks()

    elif cmd == "mark":
        mark(int(sys.argv[2]), sys.argv[3])

    elif cmd == "delete":
        delete(int(sys.argv[2]))