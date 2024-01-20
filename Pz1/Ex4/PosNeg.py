try:
    num = float(input("Num: "))
    if num > 0:
        print(1)
    elif num < 0:
        print(-1)
    else:
        print(0)
except:
    print("Wrong input.")
