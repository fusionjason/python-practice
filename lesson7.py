# dictionaries - storing data as key- value pairs

assignment = {
    "title": "module 2 quiz",
    "class": "principles of microeconomics",
    "due_date": "2026-08-30",
    "done": False
}

print(assignment["title"] + " is due " + assignment["due_date"])

assignment["done"] = True
print("marked done: " +str(assignment["done"]))


