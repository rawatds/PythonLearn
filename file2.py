try:
    with open("assert.py1", "r") as reader:
        pass
except Exception as e:
    print(e)

print("Done")