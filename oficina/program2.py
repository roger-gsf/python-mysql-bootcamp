name = input("Type your name: ")
while True:
    name = input("Type your name: ")
    if not name:
        break
    age = int(input("Type your age: "))
    print(name, "is", age, "years old.")
print("Fim")
