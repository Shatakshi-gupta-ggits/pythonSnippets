# File operation modes demonstration

# Write mode 'w': Creates file if not exists, overwrites if exists
with open('data.txt', 'w') as f:
    f.write("Hello World!")
print("File written in write mode")

# Read mode 'r': Reads from file
with open('data.txt', 'r') as f:
    content = f.read()
    print("Read content:", content)

# Append mode 'a': Adds to end of file without overwriting
with open('data.txt', 'a') as f:
    f.write("\nAppended text")
print("Text appended")

# Exclusive creation 'x': Creates new file, fails if file exists
try:
    with open('newfile.txt', 'x') as f:
        f.write("New file content")
    print("New file created")
except FileExistsError:
    print("File already exists, cannot create")

# Read and write 'r+': Can read and write, starts from beginning
with open('data.txt', 'r+') as f:
    existing = f.read()
    print("Existing content:", existing)
    f.write("\nAdded via r+ mode")
    f.seek(0)  # Go back to start to read all
    updated = f.read()
    print("Updated content:", updated)
