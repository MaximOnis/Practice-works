"""
2. Напишіть функцію, яка зчитує з клавіатури числа і перемножує їх до тих пір,
поки не буде введений 0. Функція повинна повертати в результат множення.
Викличте функцію і виведіть на екран результат її роботи.
"""

def mult():
    try:
        a = float(input("First number:"))
        b = float(input("Second number:"))
        return a * b
    except ValueError:
        print("Wrong input.")
        return 1


res = mult()
print(res)
while not res == 0:
    res = mult()
    print(res)