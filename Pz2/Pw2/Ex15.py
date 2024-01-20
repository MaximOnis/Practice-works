"""
5. В основній гілці програми викличте першу функцію. Те, що вона повернула,
передайте в другу функцію. Якщо друга функція повернула True, то ті ж дані (з
першої функції) передайте в третю функцію, а значення, що повернене з третьої
функції передайте у четверту.
"""

# 1

def getInput():
    a = input("Input:")
    return a

# 2

def testinput(a):
    try:
        int(a)
        return True
    except:
        return False

# 3

def strToInt(a):
    try:
        return int(a)
    except:
        return None

# 4

def printInt(a):
    print(a)


a = getInput()
if testinput(a):
    printInt(strToInt(a))



