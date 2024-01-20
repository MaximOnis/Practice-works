"""
2. Вдосконалить попередню програму, обробивши виняток ValueError, що виникає,
коли вводиться не ціле число.
"""

try:
    old = int(input("Ваш вік(від 3):"))
    print('Рекомендовано:', end='')
    if 3 <= old < 6:
        print('"Заєць в лабіринті"')
    elif 6 <= old < 12:
        print('"Марсіанин"')
    elif 12 <= old < 16:
        print('"Загадковий острів"')
    elif 16 <= old:
        print('"Потік свідомості"')
    else:
        print("Неправильно введено вік.")
except ValueError:
    print("ValueError")
