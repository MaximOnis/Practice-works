string = str(input("Enter:"))
balance = 0
for s in string:
    if s.isupper():
        balance += 1
    elif s.islower():
        balance -= 1
if balance < 0:
    print(string.lower())
elif balance > 0:
    print(string.upper())
else:
    print(string)