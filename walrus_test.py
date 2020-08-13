inputs =  list()

while (cmd := input("Enter a command (quit to exit): ")) != 'quit':
    inputs.append(cmd)

print("----------------- All commands entered by user ---------------------------")
print(inputs)