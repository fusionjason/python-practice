# add assignment

assignments = []

def assignment(title, class_name, due_date):
    print("your assignment is " + title + ".")
    print("for " + class_name + " class.")
    print("and the due date is " + due_date + ".")

    new_assignment = {"title": title, "class": class_name, "due_date": due_date}
    assignments.append(new_assignment)
    print("it has been added")

while True:
    choice = input("do you want to add, list, or quit? ")

    if choice == "add":
        title = input("what ius the assignment? ")
        due_date = input("when is the due_date? ")
        class_name = input("what class is this assignment for? ")
        assignment(title, class_name, due_date)

    elif choice == "list":
        for item in assignments:
            print(item["title"] + " (" + item["class"] + ") - due " + item["due_date"])

    elif choice == "quit":
        break