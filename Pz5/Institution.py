class Institution:
    def __init__(self, name, price, type_of_payment, inst_id, debt=0):
        self.price = price
        self.debt = debt
        self.name = name
        self.type_of_payment = type_of_payment
        self.id = inst_id
        self.count = 0

    def skip_day(self):
        if self.type_of_payment == "Денна":
            self.debt += self.price
        else:
            self.count += 1
            if (self.type_of_payment == "Тижнева" and self.count == 7) or (self.type_of_payment == "Місячна" and self.count == 30) or (self.type_of_payment == "Річна" and self.count == 365):
                self.count = 0
                self.debt += self.price

    def skip_week(self):
        if self.type_of_payment == "Денна":
            self.debt += 7 * self.price
        elif self.type_of_payment == "Тижнева":
            self.debt += self.price
        else:
            self.count += 7
            if self.type_of_payment == "Місячна" and self.count >= 30:
                self.count -= 30
                self.debt += self.price
            elif self.type_of_payment == "Річна" and self.count >= 365:
                self.count -= 365
                self.debt += self.price

    def set_name(self, name):
        self.name = name

    def debt_payment(self):
        self.debt = 0

    def update_debt(self):
        self.debt += self.price

    def set_price(self, price):
        self.price = price

    def set_type_of_pay(self, payment):
        self.type_of_payment = payment

    def set_debt(self, debt):
        self.debt = debt

    def to_club(self):
        return Club(self.name, self.price, self.type_of_payment, "-", self.id, self.debt)

    def to_kindergarten(self):
        return Kindergarten(self.name, self.price, self.type_of_payment,  self.id, self.debt)

    def to_school(self):
        return School(self.name, self.price, self.type_of_payment, self.id, self.debt)

    def to_other(self):
        return OtherInst(self.name, self.price, self.type_of_payment, "-", self.id, self.debt)


class Club(Institution):
    def __init__(self, name, price, type_of_payment, inst_id, specification="-", debt=0):
        super().__init__(name, price, type_of_payment, inst_id, debt)
        self.specification = specification
        self.type = "Гурток"

    def values(self):
        return self.name, self.type, self.type_of_payment, self.price, self.debt, self.specification, self.id

    def set_specification(self, specification):
        self.specification = specification


class Kindergarten(Institution):
    def __init__(self, name, price, type_of_payment, inst_id, debt=0):
        super().__init__(name, price, type_of_payment, inst_id, debt)
        self.specification = "-"
        self.type = "Дитячий садок"

    def values(self):
        return self.name, self.type, self.type_of_payment, self.price, self.debt, self.specification, self.id


class School(Institution):
    def __init__(self, name, price, type_of_payment, inst_id, debt=0):
        super().__init__(name, price, type_of_payment, inst_id, debt)
        self.specification = "-"
        self.type = "Школа"

    def values(self):
        return self.name, self.type, self.type_of_payment, self.price, self.debt, self.specification, self.id


class OtherInst(Institution):
    def __init__(self, name, price, type_of_payment, inst_id, specification="-", debt=0):
        super().__init__(name, price, type_of_payment, inst_id, debt)
        self.specification = specification
        self.type = "Інше"

    def values(self):
        return self.name, self.type, self.type_of_payment, self.price, self.debt, self.specification, self.id

    def set_specification(self, specification):
        self.specification = specification
