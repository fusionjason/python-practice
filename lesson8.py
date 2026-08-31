# lists of dictionaries - combining both, same structure as real assignments.json

assignments = [
    {"title": "module 2 quiz", "class": "microeconomices", "done": False},
    {"title": "chapter 9 quiz", "class": "american government", "done": True},
    {"title": "sap appeal", "class": "financial aid", "done": True}
]

for item in assignments:
    status = "DONE" if item["done"] else "NOT DONE"
    print(item["title"] + " (" + item["class"] + ") - " + status)



