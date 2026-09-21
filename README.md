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
- `assignment_tracker_db.py` — the same features as `assignment_tracker.py`, rebuilt on a real **SQLite database** instead of a JSON file. Every action (add, update, delete) commits immediately, so nothing is lost even if the program closes mid-session — a real upgrade over the JSON version, which only saved on quit. Uses parameterized SQL queries (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) instead of looping through a Python list by hand, the same approach used in production applications. Every function takes its database connection as a parameter (dependency injection), so each one can be tested without touching the real database. Run it with `python assignment_tracker_db.py`.

## Testing

Automated tests for the SQLite tracker are in `test_basic.py` and run with [pytest](https://pytest.org).

**Run them:**

```
pip install pytest
pytest test_basic.py
```

Expected result: `12 passed` (3 warm-up tests on small helper functions, plus 9 database tests).

**What is tested:**

- All nine database functions in `assignment_tracker_db.py`: `add_assignment`, `list_assignments`, `delete_assignment`, `done`, `not_done`, `filter_by_class`, `edit_due_date`, `delete_by_class`, and `mark_class_done`.
- Each test builds its own throwaway in-memory SQLite database (`sqlite3.connect(":memory:")`), so tests always start from clean, known data and never touch the real `assignment.db`.
- Functions that only print (`list_assignments`, `filter_by_class`) are tested with pytest's `capsys` fixture, which captures printed output. The filter test checks that the right assignment appears and that the other class's assignment does not.
- Update-style functions (`done`, `not_done`, `edit_due_date`, `mark_class_done`) are verified by querying the database afterward. The `not_done` test first marks an assignment done, so it proves the value really changes back.

**What I learned building these tests:**

- Refactoring functions to accept a connection parameter, instead of relying on a global one, is what made them testable.
- Putting the menu loop under `if __name__ == "__main__":` keeps it from running when the file is imported. Without it, importing the module into the tests launched the interactive menu and crashed the test run.
