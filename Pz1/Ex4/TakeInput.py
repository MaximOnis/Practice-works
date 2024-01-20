data = input("Type something: ")
print(data.isspace())
if not data == "" and not data.isspace():
    print("OK.")
    print(data)
