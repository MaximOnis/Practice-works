"""
Напишіть програму, яка запитує введення двох значень. Якщо хоча б одне з них
не є числом, то повинна виконуватися конкатенація, тобто з`єднання, рядків. В інших
випадках введені числа підсумовуються.
"""

a = input("a:")
b = input("b:")
try:
    a = int(a)
    b = int(b)
    print(a + b)
except:
    a = str(a)
    b = str(b)
    print(a + b)