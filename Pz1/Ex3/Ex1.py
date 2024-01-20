
firstVar = 34
secondVar = 10

thirdVar = 10
fourthVar = 8.4

print(secondVar == thirdVar and firstVar != fourthVar)
# True * True = True
print(firstVar == secondVar and thirdVar > fourthVar and secondVar <= thirdVar)
# False * True * True = False

print(thirdVar > firstVar or secondVar == thirdVar or firstVar != fourthVar)
# False + True + True = True
print(secondVar == fourthVar or thirdVar > firstVar)
# False + False = False

print(thirdVar == "cat" or thirdVar == "thirdVar" or "second" < "secondVar")
# False + False + True = True
print(firstVar == "firstVar" and secondVar == "10" and firstVar > secondVar)
# False * False * True = False

# 2
print("====================#2====================")
while 1:
    try:
        firstVar = float(input("First = "))
        secondVar = float(input("Second = "))
        print(firstVar > secondVar)
        break
    except:
        print("Wrong input.")
