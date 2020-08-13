class Alphabet:

    def __init__(self, value):
        self._value = value

    # Getter
    def getValue(self):
        return self._value

    #Setter
    def setValue(self, value):
        self._value = value

    # Deleter
    def delValue(self):
        del self._value

    # Assign the getter, setter, and deleter
    value = property(getValue, setValue, delValue)

alpha = Alphabet("Hello")
print(alpha.value)

Alphabet.value = "World"
print(alpha.value)

del alpha.value
print(alpha.value)


