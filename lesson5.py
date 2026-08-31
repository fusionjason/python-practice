# reading and writing files - open(), with, .write(), >read()

with open("notes.txt", "w") as f:
    f.write("learning Python\n")
    f.write("lesson 5: files\n")
    f.write("this is fun\n")
    f.write("what is next?\n")

with open("notes.txt", "r") as f:
    contents = f.read()
    print(contents)

