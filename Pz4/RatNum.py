
import math


class ZeroDivi(Exception):
    def __init__(self):
        super().__init__("Ploxo")


class RatNum:
    # int numerator - чисельник
    # int denominator - знаменник
    def __init__(self, numerator, denominator):
        # перевірка чи може бути дріб і спрощення
        if numerator > 0 > denominator:
            self.numerator = numerator * -1
            self.denominator = math.fabs(denominator)
        elif numerator < 0 and denominator < 0:
            self.numerator = math.fabs(numerator)
            self.denominator = math.fabs(denominator)
        elif numerator == 0 or denominator == 0:
            self.numerator = 0
            self.denominator = 0
        else:
            self.numerator = numerator
            self.denominator = denominator
            # скорочення
        RatNum.simplification(self)

    def simplification(self):
        div = math.gcd(int(self.numerator), int(self.denominator))
        if self.numerator != 0 and self.denominator != 0 and div != 1:
            self.denominator /= div
            self.numerator /= div
            self.numerator = int(self.numerator)
            self.denominator = int(self.denominator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        if self.denominator == other.denominator:
            numerator = self.numerator + other.numerator
            denominator = self.denominator
        else:
            denominator = math.lcm(self.denominator, other.denominator)
            numerator = int(self.numerator * (denominator / self.denominator) + other.numerator * (denominator / other.denominator))
        return RatNum(numerator, denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            numerator = self.numerator - other.numerator
            denominator = self.denominator
        else:
            denominator = math.lcm(self.denominator, other.denominator)
            numerator = int(self.numerator * (denominator / self.denominator) - other.numerator * (denominator / other.denominator))
        return RatNum(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return RatNum(numerator, denominator)

    def __truediv__(self, other):
        if self.numerator == 0 or other.numerator == 0:
            return RatNum(0, 0)
        else:
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return RatNum(numerator, denominator)