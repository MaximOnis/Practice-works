# 2

while 1:
    try:
        print("=========Приклад=========")
        res = float(input("4 * 100 - 54 = "))
        corrRes = 4 * 100 - 54
        print("Ваша відповідь:", res)
        print("Правильна відповідь:", corrRes)
        if res == corrRes:
            print("Відповідь правильна ^_^")
        else:
            print("Відповідь неправильна >_<")
        break
    except:
        print("Відповідь введено некорректно.")
# 3
while 1:
    try:
        firstNum = float(input("firstNum = "))
        break
    except:
        print("Введіть корректну відповідь!")
while 1:
    try:
        secondNum = float(input("secondNum = "))
        break
    except:
        print("Введіть корректну відповідь!")
while 1:
    try:
        thirdNum = float(input("thirdNum = "))
        break
    except:
        print("Введіть корректну відповідь!")
while 1:
    try:
        fourthNum = float(input("fourthNum = "))
        break
    except:
        print("Введіть корректну відповідь!")

firstSum = firstNum + secondNum
secondSum = thirdNum + fourthNum
print(f"firstSum = {firstSum:.2f} \nsecondSum = {secondSum:.2f} \nResult = {firstSum / secondSum:.2f}")
