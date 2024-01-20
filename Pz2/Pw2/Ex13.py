"""
3. Функція strToInt має один параметр. У тілі перетворює передане значення до
целочисленному типу. Повертає отримане число.
"""


def strToInt(a):
    try:
        return int(a)
    except:
        return None


print(strToInt("23"))
print(strToInt("fsd"))

