# Task Tracker CLI

A lightweight command-line task manager built in Python.
Supports task creation, updates, deletion, and status tracking with timestamps.

---

## Features

* Add tasks
* Update task description
* Delete tasks
* Mark tasks (`todo`, `inprogress`, `done`)
* Automatic timestamps (`createdAt`, `updatedAt`)
* Persistent storage using JSON

---

## Installation

```bash
git clone <https://github.com/hadeed-wsy/task-tracker-cli/tree/main>
cd task-tracker-cli
```

---

## Usage

Run commands using:

```bash
python main.py <command> [arguments]
```

---

## Commands

### Add task

```bash
python main.py add "buy ice cream"
```

### List tasks

```bash
python main.py list
```

### Update task

```bash
python main.py update 1 "buy chocolate"
```

### Delete task

```bash
python main.py delete 1
```

### Mark status

```bash
python main.py mark 1 todo
python main.py mark 1 inprogress
python main.py mark 1 done
```

---

## Task Structure

```json
[
  {
    "id": 1,
    "description": "buy chocolate",
    "status": "todo",
    "createdAt": "2026-04-08 18:11:23",
    "updatedAt": "2026-04-08 18:11:23"
  }
]
```

---

## Notes

* Data is stored in `tasks.json`
* IDs are auto-generated
* Status must be: `todo`, `inprogress`, or `done`

---

## Limitations

* No input validation (may crash on invalid input)
* Uses index-based operations
* No filtering (e.g., `list done`)

---

