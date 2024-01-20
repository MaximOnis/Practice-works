name = input("What`s your name?: ").capitalize()
try:
    age = int(input(" How old are you?: "))
    place = input("Where you from?: ").capitalize()
    print("This is", name)
    print("It is", age)
    print("S(he) lives in", place)
except:
    print("Something went wrong.")
    place = input("Where you from?: ").capitalize()
    print("This is", name)
    print("S(he) lives in", place)
