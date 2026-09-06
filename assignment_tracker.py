# assignment tracker with save/load, mark done/not done, sorting, deleting, filtering, editing due date, delete by class and mark class done.

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

def get_due_date(item):
    return item["due date"]

while True:
    choice = input("do you want to add, list, quit, not done, done, delete, filter, edit due date, delete class, and mark class done? ")

    if choice == "add":
        line = input("what is the assignment, class, and due date? (separate multiple with semicolons) ").strip()
        entries = line.split(";")
        for entry in entries:
            parts = entry.split(",")
            title = parts[0].strip()
            class_name = parts[1].strip()
            due_date = parts[2].strip()
            assignment(title, class_name, due_date)

    elif choice == "list":
        if not assignments:
                print("no assignments found")
        else:
            sorted_assignments = sorted(assignments, key=get_due_date)
            for item in sorted_assignments:
                status = "DONE" if item["done"] else "NOT DONE"
                print(item["title"] + " (" + item["class"] + ") - due " + item["due date"] + " - " + status)


    elif choice == "quit":
        with open("my_assignments.json", "w") as f:
            json.dump(assignments, f)
        break

    elif choice == "done":
        which = input("which assignment(s) is done? (separate multiple with comma) ").strip()
        names = which.split(",")
        for name in names:
            name = name.strip()
            for item in assignments:
                if item["title"].lower() == name.lower():
                    item["done"] = True
                    print("marked done:", name)

    elif choice == "not done":
        which = input("which assignment(s) is not done? (separtate multiple with comma) ").strip()
        names = which.split(",")
        for name in names:
            name = name.strip()
            for item in assignments:
                if item["title"].lower() == name.lower():
                    item["done"] = False
                    print("marked not done:", name)

    elif choice == "delete":
        which = input("which assignment(s) do you want to delete? (separate multiple with comma) ").strip()
        names = which.split(",")
        for name in names:
            name = name.strip()
            for item in assignments:
                if item["title"].lower() == name.lower():
                    assignments.remove(item)
                    print("deleted:", name)
                    break

    elif choice == "filter":
        which_class = input("which class do you want to see? ").strip()
        found_any = False
        for item in assignments:
            if item["class"].lower() == which_class.lower():
                found_any = True
                status = "DONE" if item["done"] else "NOT DONE"
                print(item["title"] + " (" + item["class"] + ") - due " + item["due date"] + " - " + status)
        if not found_any:
            print("no assignments found for class:", which_class)

    elif choice == "edit due date":
        which = input("which assignment(s) needs the due date changed? (separate multiple with comma) " ).strip()
        names = which.split(",")
        for name in names:
            name = name.strip()
            for item in assignments:
                if item["title"].lower() == name.lower():
                    new_date = input("what is the new due date for " + name + "? ").strip()
                    item["due date"] = new_date
                    print("updated due date for:", name)

    elif choice == "delete class":
        which_class = input("which class(s) do you want to delete all assignments for? (separate multiple with comma) ").strip()
        raw_names = which_class.split(",")
        class_names = []
        for n in raw_names:
            class_names.append(n.strip().lower())
        remaining = []
        for item in assignments:
            if item["class"].lower() not in class_names:
                remaining.append(item)
        assignments = remaining
        print("deleted all assignments for:", which_class)

    elif choice == "class done":
        which_class = input("which class(s) do you want to mark all done? (separate multiple with a coma) ").strip()
        found_any = False
        for item in assignments:
            if item["class"].lower() == which_class.lower():
                item["done"] = True
                found_any = True
        if found_any:
            print("marked all assingments done for:", which_class)
        else:
            print("no assingments found for that class:")

    else:
        print("that's not a valid option, please try again")
