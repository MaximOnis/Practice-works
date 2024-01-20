""" варіант 17: У матриці М(4,6) визначити максимальний і мінімальний елементи
та їхні індекси.

"""

import numpy as np

class Matrix:
    rows = 0
    columns = 0
    matrix = np.array(int)

    def __init__(self):
        self.rows = 4
        self.columns = 6
        self.matrix = np.random.randint(0, 21, size=(self.rows, self.columns))

    def printMatrix(self):
        print("=================Matrix================")
        print(self.matrix)
        print("=======================================")

    def getMax(self):
        indexes = np.argwhere(self.matrix == np.max(self.matrix))
        indexes = np.add(indexes, 1)
        print(f"Максимальний елемент матриці: {self.matrix.max()}, індекси:", end=" ")
        for i in indexes:
            print(i, end=" ")
        print()

    def getMin(self):
        indexes = np.argwhere(self.matrix == np.min(self.matrix))
        indexes = np.add(indexes, 1)
        print(f"Мінімальний елемент матриці: {self.matrix.min()}, індекси:", end=" ")
        for i in indexes:
            print(i, end=" ")
        print()


mat = Matrix()
mat.printMatrix()
mat.getMax()
mat.getMin()
res = True
while res:
    response = input("Хочете ще раз спробувати?: ").lower()
    if response == "так":
        mat = Matrix()
        mat.printMatrix()
        mat.getMax()
        mat.getMin()
    elif response == "ні":
        print("Бувай!!!")
        res = False
    else:
        print("Введіть \"так\", або \"ні\"")