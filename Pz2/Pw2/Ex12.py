"""
2. Функція testInput має один параметр. У тілі вона перевіряє, чи можна передане
їй значення перетворити до цілого числа. Якщо можна, повертає логічне True.
Якщо не можна - False.
"""


def testinput(a):
    try:
        int(a)
        return True
    except:
        return False


print(testinput("r"))
print(testinput("2"))
print(testinput(2))
print(testinput(23.34))

