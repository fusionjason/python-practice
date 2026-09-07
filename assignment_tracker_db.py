# assignment tracker using a real SQLite database instead of JSON, with save/load, mark done/not done, sorting, deleting, filtering, editing due date, delete by class and mark class done.

import sqlite3
conn = sqlite3.connect("assignment.db")        # opens (or creates) the database file
cursor = conn.cursor()                         # the cursor is what actually runs SQL commands.
cursor.execute("""CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    class TEXT,
    due_date TEXT,
    done INTEGER
)"""
)
conn.commit()                                   # commits the changes to the database.

# everything below this is the code for a database connection.

def add_assignment(title, class_name, due_date):
    cursor.execute("INSERT INTO assignments (title, class, due_date, done) VALUES (?, ?, ?, ?)", (title, class_name, due_date, 0))
    conn.commit()

def list_assignments():
    cursor.execute("SELECT * FROM assignments ORDER BY due_date")
    rows = cursor.fetchall()
    if not rows:
        print("no assignments found")
    else:
        for row in rows:
            status = "DONE" if row[4] else "NOT DONE"
            print(f"{row[1]} ({row[2]}) - due {row[3]} - {status}")

def delete_assignment(title):
    cursor.execute("DELETE FROM assignments WHERE title = ?", (title,))
    conn.commit()

def mark_done(title):
    cursor.execute("UPDATE assignments SET done = 1 WHERE title = ?", (title,))
    conn.commit()                                                               # UPDATE, setting done = 1, where title matches

def mark_not_done(title):
    cursor.execute("UPDATE assignments SET done = 0 WHERE title = ?", (title,))
    conn.commit()                                                               # UPDATE, setting done = 0, where title matches

def filter_by_class(class_name):
    cursor.execute("SELECT * FROM assignments WHERE class = ?", (class_name,))
    rows = cursor.fetchall()
    if not rows:
        print(f"no assignments found for class: {class_name}")
    else:
        for row in rows:
            status = "DONE" if row[4] else "NOT DONE"
            print(f"{row[1]} ({row[2]}) - due {row[3]} - {status}")

def edit_due_date(title, new_due_date):
    cursor.execute("UPDATE assignments SET due_date = ? WHERE title = ?", (new_due_date, title))
    conn.commit()

def delete_by_class(class_name):
    cursor.execute("DELETE FROM assignments WHERE class = ?", (class_name,))
    conn.commit()                                                             # same shape as delete_assingment, but matching class instead of title.

def mark_class_done(class_name):
    cursor.execute("UPDATE assignments SET done = 1 WHERE class = ?", (class_name,))
    conn.commit()                                                             # same shape as mark_done, but matching class instead of title.

# everything below this is for the menu loop.

while True:
    choice = input("do you want to add, list, delete, mark done, mark not done, filter by class, edit due date, delete by class, mark class done or quit? ").lower()

    if choice == "add":
        line = input("what is the assignment, class, and due date? (separate multiple with semicolons) ").strip()
        entries = line.split(";")
        for entry in entries:
            parts = entry.split(",")
            title = parts[0].strip()
            class_name = parts[1].strip()
            due_date = parts[2].strip()
            add_assignment(title, class_name, due_date)

    elif choice == "list":
        list_assignments()

    elif choice == "quit":
        break

    elif choice == "done":
        which = input("enter assignment titles to mark as done (comma-separated): ")
        for name in which.split(","):
            name = name.strip()                         # have to ask for the tile with (input...)  then finish with mark_done(title)
            mark_done(name)

    elif choice == "not done":
        which = input("enter assignment titles to mark as not done (comma-separated): ")
        for name in which.split(","):
            name = name.strip()                         # have to ask for the tile with (input...)  then finish with mark_not_done(title)
            mark_not_done(name)

    elif choice == "delete":
        which = input("enter assignment titles to delete (comma-separated): ")
        for name in which.split(","):
            name = name.strip()                         # have to ask for the tile with (input...)  then finish with delete_assignment(title)
            delete_assignment(name)

    elif choice == "filter by class":
        which = input("enter class name to filter by: ")
        for name in which.split(","):
            name = name.strip()
            filter_by_class(name)

    elif choice == "edit due date":
        title = input("enter assignment title to edit due date: ")
        new_due_date = input("enter new due date (mm-dd-yyyy):")
        edit_due_date(title, new_due_date=new_due_date)

    elif choice == "delete by class":
        class_name = input("enter class name to delete all assignments: ")
        delete_by_class(class_name)

    elif choice == "mark class done":
        class_name = input("enter class name to mark all assignments as done: ")
        mark_class_done(class_name)
