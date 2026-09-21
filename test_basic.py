import sqlite3
from assignment_tracker_db import add_assignment
from assignment_tracker_db import list_assignments
from assignment_tracker_db import delete_assignment
from assignment_tracker_db import done
from assignment_tracker_db import not_done
from assignment_tracker_db import filter_by_class
from assignment_tracker_db import edit_due_date
from assignment_tracker_db import delete_by_class
from assignment_tracker_db import mark_class_done


def calculate_percentage(part, whole):
    return (part / whole) * 100

def test_calculate_percentage():
    assert calculate_percentage(25, 50 ) == 50.0
    assert round(calculate_percentage(2,3), 2) == 66.67


def get_status(done):
        return "DONE" if done else "NOT DONE"

def test_get_status_done():
     assert get_status(1) == "DONE"

def test_get_status_not_done():
     assert get_status(0) == "NOT DONE"

def test_add_assignment():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        class TEXT,
        due_date TEXT,
        done INTEGER
    )""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()
    assert len(rows) == 1
    assert rows[0][1] == "test quiz"

def test_list_assignmnets(capsys):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       title TEXT,
       class TEXT,
       due_date TEXT,
       done INTEGER
)""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    list_assignments(conn)

    captured = capsys.readouterr()
    assert "test quiz" in captured.out

def test_delete_assignments(capsys):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        class TEXT,
        due_date TEXT,
        done INTEGER
)""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    delete_assignment(conn, "test quiz")
    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()
    assert len(rows) == 0

def test_done(capsys):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        class TEXT,
        due_date TEXT,
        done INTEGER
)""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    done(conn, "test quiz")
    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()
    assert rows[0][4] == 1

def test_not_done(capsys):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        class TEXT,
        due_date TEXT,
        done INTEGER
)""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    done(conn, "test quiz")
    not_done(conn, "test quiz")
    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()
    assert rows[0][4] == 0

def test_filter_by_class(capsys):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        class TEXT,
        due_date TEXT,
        done INTEGER
)""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    add_assignment(conn, "test quiz 2", "history", "12/10/2026")
    filter_by_class(conn, "math")

    captured = capsys.readouterr()
    assert "test quiz" in captured.out
    assert "test quiz 2" not in captured.out

def test_edit_by_date(capsys):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        class TEXT,
        due_date TEXT,
        done INTEGER
)""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    edit_due_date(conn, "test quiz", "11/15/2026")
    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()
    assert rows[0][3] == "11/15/2026"

def test_delete_by_class(capsys):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        class TEXT,
        due_date TEXT,
        done INTEGER
)""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    add_assignment(conn, "module 1", "math", "12/20/2026")
    add_assignment(conn, "test quiz 2", "history", "12/10/2026")
    delete_by_class(conn, "math")
    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()
    assert len(rows) == 1

def test_mark_class_done(capsys):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        class TEXT,
        due_date TEXT,
        done integer
)""")

    add_assignment(conn, "test quiz", "math", "12/01/2026")
    add_assignment(conn, "module 1", "math", "12/20/2026")
    add_assignment(conn, "test quiz 2", "history", "12/10/2026")
    mark_class_done(conn, "math")
    cursor.execute("SELECT * FROM assignments")
    rows = cursor.fetchall()
    assert rows[0][4] == 1
    assert rows[1][4] == 1
    assert rows[2][4] == 0