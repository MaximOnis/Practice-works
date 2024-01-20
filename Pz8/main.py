"""

       * *                    * * *                   * * * *
       * *                    * * *                   * * * *
       * *                    * * *                   * * * *
       * *                    * * *                   * * * *
        *                      * *                     * * *
* * * * * * * * *      * * * * * * * * * *     * * * * * * * * * * *
    * * * * *              * * * * * *             * * * * * * *
        *                      ***                     * * *

"""


def get_width():
    while True:
        try:
            width = int(input("Width(min - 9):"))
            if width >= 9:
                return width
            print("Too small number.")
        except ValueError:
            print("Wrong input.")


def draw(w):
    for b in range(4):
        print("       *", end="")
        for a in range(w-8):
            print(" *", end="")
        print("       \n", end="")
    print("        *", end="")
    for a in range(w-9):
        print(" *", end="")
    print("        \n", end="")
    for a in range(w):
        print("* ", end="")
    print(" \n   ", end="")
    for a in range(w-4):
        print(" *", end="")
    print("    \n        *", end="")
    for a in range(w-9):
        print(" *", end="")
    print("        ")


res = get_width()
draw(res)
