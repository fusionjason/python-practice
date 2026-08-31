# this is the save/load a file and also mark done for adding assignments to a tracker

import json

try:
    with open("my_assignments.json", "r") as f:
        assignments = json.load(f)
except FileNotFoundError:
    assignments = []


def assignment(title, class_name, due_date):
    print("your assignment is " + title + ".")
    print("for " + class_name + " class.")
    print("and the due date is " + due_date + ".")

    new_assignment = {"title": title, "class": class_name, "due date": due_date, "done": False}
    assignments.append(new_assignment)
    print("it has been added")

while True:
    choice = input("do you want to add, list, quit, or done? ")

    if choice == "add":
        title = input("what is the assignment? ").strip()
        due_date = input("when is the due date? ").strip()
        class_name = input("what class is this assignment for? ").strip()

        assignment(title, class_name, due_date)

    elif choice == "list":
        for item in assignments:
            status = "DONE" if item["done"] else "NOT DONE"
            print(item["title"] + " (" + item["class"] + ") - due " + item["due date"] + " - " + status)


    elif choice == "quit":
        with open("my_assignments.json", "w") as f:
            json.dump(assignments, f)
        break

    elif choice == "done":
        which = input("which assignment is done? ").strip()
        for item in assignments:
            if item["title"] == which:
                item["done"] = True
                print("marked done")
