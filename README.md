# Python Practice

My Python learning journey, working toward a software developer career alongside my business background.

## Lessons

Small hands-on exercises covering the fundamentals, in order:

- `lesson1.py` — variables, strings, `input()`
- `lesson2.py` — `if`/`elif`/`else`
- `lesson3.py` — `for` loops with `range()`
- `lesson4.py` — functions (`def`)
- `lesson5.py` — reading and writing files
- `lesson6.py` — lists
- `lesson7.py` — dictionaries
- `lesson8.py` — lists of dictionaries

## Capstone: Assignment Tracker

A menu-driven assignment tracker, rebuilt several times as I picked up new skills:

- `project.py` — first attempt: collects one assignment and prints it back.
- `project2.py` — full version: a menu-driven tracker (add / list / mark done / quit) that saves and loads from a JSON file, so data persists between runs. Built the same way my own [Jarvis assistant](https://github.com/fusionjason/jarvis) tracks assignments, just simplified.
- `project3.py` — adds sorting by due date and a "not done" option to undo a completed mark.
- `assignment_tracker.py` — full-featured version: adding multiple assignments at once, filtering by class, editing due dates, deleting by title or by whole class, and marking an entire class done at once.
- `assignment_tracker_db.py` — the same features as `assignment_tracker.py`, rebuilt on a real **SQLite database** instead of a JSON file. Every action (add, update, delete) commits immediately, so nothing is lost even if the program closes mid-session — a real upgrade over the JSON version, which only saved on quit. Uses parameterized SQL queries (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) instead of looping through a Python list by hand, the same approach used in production applications.
