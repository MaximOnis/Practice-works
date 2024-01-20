"""
17 варіант

Завдання: Обчислити і вивести на екран у табличному вигляді значення
функції f(x) на заданому інтервалі зміни значень аргумента х від xпоч до xкін з
кроком h. Коефіцієнти a, b, c – дійсні числа.
Значення a, b, c, xпоч, xкін та h вводити з клавіатури. Передбачити перевірку
допустимості введених значень та ОДЗ функції.

"""
import math

from tabulate import tabulate
def getData():
    data = []
    while(1):
        try:
            data.append(float(input("a: ")))
            break
        except ValueError:
            print("Значення введено неправильно. Спробуйте ще раз")
    while (1):
        try:
            data.append(float(input("b: ")))
            break
        except ValueError:
            print("Значення введено неправильно. Спробуйте ще раз")
    while (1):
        try:
            data.append(float(input("c: ")))
            break
        except ValueError:
            print("Значення введено неправильно. Спробуйте ще раз")
    while (1):
        try:
            h = float(input("h: "))
            if h == 0:
                print("Крок не повинен дорівнювати нулю.")
                continue
            data.append(h)
            break
        except ValueError:
            print("Значення введено неправильно. Спробуйте ще раз")
    while (1):
        try:
            x1 = float(input("x1: "))
            break
        except ValueError:
            print("Значення введено неправильно. Спробуйте ще раз")
    while (1):
        try:
            x2 = float(input("x2: "))
            if x1 > x2 and h > 0:
                temp = x1
                x1 = x2
                x2 = temp
            elif x2 > x1 and h < 0:
                temp = x1
                x1 = x2
                x2 = temp
            elif x1 == x2:
                continue
            data.append(x1)
            data.append(x2)
            break
        except ValueError:
            print("Значення введено неправильно. Спробуйте ще раз")
    return data

def Calc():
    data = getData()
    x1 = data[4]
    x2 = data[5]
    h = data[3]
    a = data[0]
    b = data[1]
    c = data[2]
    del data
    dat = []
    while (h > 0 and x1 <= x2) or (h < 0 and x1 >= x2):
        if x1 < 2 and a * c < 0:
            try:
                res = (x1, round(((b * x1 + x1 * x1) / (2 * a - x1)), 2), 1)
            except:
                res = (x1, "None", 1)
            dat.append(res)
        elif x1 > 2 and c >= 0:
            try:
                res = (x1, round((math.sqrt(b + math.pow(x1, 3)) + 2 * x1 * x1), 2), 2)
            except:
                res = (x1, "None", 2)
            dat.append(res)
        else:
            try:
                res = (x1, round((((x1 * x1 * (x1 + 1)) / (x1 + 4)) + (c - 2) * (c - 2)), 2), 3)
            except:
                res = (x1, "None", 3)
            dat.append(res)
        x1 = x1 + h
    head = ["x", "Result", "№ випадку"]
    print(tabulate(dat, headers=head, tablefmt="grid"))

Calc()
