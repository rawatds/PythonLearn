# Read the file contents

with open('fruits.txt') as reader:
    fruits = reader.readlines();

print("Fruits: ", fruits)

# write to another file after reversing

with open("fruits_rev1.txt", "w") as writer:
    writer.writelines(reversed(fruits))

# Alternatively
with open("fruits_rev2.txt", "w") as writer:
    for fruit in reversed(fruits):
        writer.write(fruit)

# Appending to a file

with open("fruits.txt", "a") as appender:
    appender.write("Papaya\n")


