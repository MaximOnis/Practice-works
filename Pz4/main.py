"""
Клас RatNum імітує роботу зі звичайними дробами. Полями цього класу повинні бути два поля типу int: чисельник і знаменник дробу.
Передбачити конструктор класу та методи, що будуть ініціалізувати об’єкти класу, додавати і віднімати два дроби,
а також виводити на екран значення у форматі a/b.
"""

from RatNum import RatNum


def commands():
    print("===========================Список команд==============================")
    print("1 - вивести список команд\n2 - вивести список дробів\n3 - створити новий дріб\n4 - видалити дріб"
          "\n5 - додати два дроби\n6 - відняти два дроби\n7 - помножити два дроби\n8 - поділити два дроби"
          "\n9 - очистити консоль\n10 - вийти")
    print("======================================================================")


def printList(listOfRatNums):
    print("===========================Список дробів==============================")
    for num in range(len(listOfRatNums)):
        print(num+1, ". ", listOfRatNums[num], sep="")
    print("======================================================================")


def chooseRatNum(listOfRatNums):
    try:
        response = int(input("Введіть номер дробу зі списку:"))
        return listOfRatNums[response - 1]
    except:
        print("Такого дробу не існує!")


def addToList(ratnum, listOfRatNums):
    while True:
        try:
            response = int(input("Зберегти цей дріб?(1 - так, 2 - ні): "))
            if response == 1:
                listOfRatNums.append(ratnum)
                print("Додано.")
                break
            elif response == 2:
                print("Не додано.")
                break
            else:
                print("Введіть 1 або 2!")
                continue
        except:
            print("Введіть 1 або 2!")


def add(listOfRatNums):
    print("=========================Вибір для додавання=============================")
    a = chooseRatNum(listOfRatNums)
    b = chooseRatNum(listOfRatNums)
    try:
        res = a + b
        print("Результат: ", res)
        addToList(res, listOfRatNums)
    except:
        pass



def sub(listOfRatNums):
    print("=========================Вибір для віднімання=============================")
    a = chooseRatNum(listOfRatNums)
    b = chooseRatNum(listOfRatNums)
    try:
        res = a - b
        print("Результат: ", res)
        addToList(res, listOfRatNums)
    except:
        pass


def div(listOfRatNums):
    print("=========================Вибір для ділення=============================")
    a = chooseRatNum(listOfRatNums)
    b = chooseRatNum(listOfRatNums)
    try:
        res = a / b
        print("Результат: ", res)
        addToList(res, listOfRatNums)
    except:
        pass


def mult(listOfRatNums):
    print("=========================Вибір для множення=============================")
    a = chooseRatNum(listOfRatNums)
    b = chooseRatNum(listOfRatNums)
    try:
        res = a * b
        print("Результат: ", res)
        addToList(res, listOfRatNums)
    except:
        pass


def deleteRatNum(listOfRatNums):
    try:
        response = int(input("Введіть номер дробу зі списку:"))
        listOfRatNums.pop(response - 1)
    except:
        print("Такого дробу не існує!")


def createRatNum(listOfRatNums):
    try:
        num = int(input("Введіть чисельник: "))
        den = int(input("Введіть знаменник: "))
        ratnum = RatNum(num, den)
        listOfRatNums.append(ratnum)
    except:
        print("Неправильно введено чисельник або знаменник!")


if __name__ == '__main__':
    list = [RatNum(1, 2), RatNum(1, 5)]
    response = "y"
    printList(list)
    commands()
    while not response == 10:
        try:
            print("======================================================================")
            response = int(input("Що ви хочете зробити?:"))
            print("======================================================================")
            match response:
                case 1:
                    commands()
                case 2:
                    printList(list)
                case 3:
                    createRatNum(list)
                case 4:
                    deleteRatNum(list)
                case 5:
                    add(list)
                case 6:
                    sub(list)
                case 7:
                    mult(list)
                case 8:
                    div(list)
                case 9:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                case 10:
                    print("Бувай!")
                case _:
                    print("Невідома команда!")
        except:
            print("Невідома команда!")

