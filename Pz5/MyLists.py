import pandas as pd


class List:
    def __init__(self):
        self.table = pd.Series()
        self.table_of_clubs = pd.Series()
        self.table_of_kindergartens = pd.Series()
        self.table_of_schools = pd.Series()
        self.table_of_other_insts = pd.Series()

    def skip_day(self):
        for element in self.table:
            self.table.loc[element.id].skip_day()

    def skip_week(self):
        for element in self.table:
            self.table.loc[element.id].skip_week()

    def pay(self, inst_id):
        self.table.loc[inst_id].debt_payment()

    def edit_name(self, inst_id, name):
        self.table.loc[inst_id].set_name(name)

    def edit_type(self, inst_id, inst_type):
        match inst_type:
            case "Школа":
                self.table.loc[inst_id] = self.table.loc[inst_id].to_school()
                self.add_school(self.table.loc[inst_id])
            case "Гурток":
                self.table.loc[inst_id] = self.table.loc[inst_id].to_club()
                self.add_club(self.table.loc[inst_id])
            case "Дитячий садок":
                self.table.loc[inst_id] = self.table.loc[inst_id].to_kindergarten()
                self.add_kindergarten(self.table.loc[inst_id])
            case "Інше":
                self.table.loc[inst_id] = self.table.loc[inst_id].to_other()
                self.add_other_inst(self.table.loc[inst_id])

    def edit_price(self, inst_id, price):
        self.table.loc[inst_id].set_price(price)

    def edit_payment(self, inst_id, payment):
        self.table.loc[inst_id].set_type_of_pay(payment)

    def edit_debt(self, inst_id, debt):
        self.table.loc[inst_id].set_debt(debt)

    def edit_spec(self, inst_id, spec):
        if self.table.loc[inst_id].type == "Школа" or self.table.loc[inst_id].type == "Дитячий садок":
            return
        else:
            self.table.loc[inst_id].set_specification(spec)

    def add_inst(self, inst):
        self.table.loc[inst.id] = inst
        if inst.type == "Школа":
            self.add_school(inst)
        elif inst.type == "Гурток":
            self.add_club(inst)
        elif inst.type == "Дитячий садок":
            self.add_kindergarten(inst)
        elif inst.type == "Інше":
            self.add_other_inst(inst)

    def add_club(self, club):
        self.table_of_clubs.loc[club.id] = club

    def add_school(self, school):
        self.table_of_schools.loc[school.id] = school

    def add_kindergarten(self, kinder):
        self.table_of_kindergartens.loc[kinder.id] = kinder

    def add_other_inst(self, other):
        self.table_of_other_insts.loc[other.id] = other

    def delete_inst(self, inst_id):
        self. table = self.table.drop(inst_id)
        try:
            self.table_of_clubs = self.table_of_clubs.drop(inst_id)
        except KeyError:
            pass
        try:
            self.table_of_schools = self.table_of_schools.drop(inst_id)
        except KeyError:
            pass
        try:
            self.table_of_kindergartens = self.table_of_kindergartens.drop(inst_id)
        except KeyError:
            pass
        try:
            self.table_of_other_insts = self.table_of_other_insts.drop(inst_id)
        except KeyError:
            pass

    def print_clubs(self):
        text = pd.DataFrame(columns=['Назва', 'Тип', 'Тип оплати', 'Ціна', 'Заборгованість', 'Специфікація', 'id'])
        for element in self.table_of_clubs:
            text.loc[element.id] = element.values()
        return text

    def print_schools(self):
        text = pd.DataFrame(columns=['Назва', 'Тип', 'Тип оплати', 'Ціна', 'Заборгованість', 'Специфікація', 'id'])
        for element in self.table_of_schools:
            text.loc[element.id] = element.values()
        return text

    def print_kindergartens(self):
        text = pd.DataFrame(columns=['Назва', 'Тип', 'Тип оплати', 'Ціна', 'Заборгованість', 'Специфікація', 'id'])
        for element in self.table_of_kindergartens:
            text.loc[element.id] = element.values()
        return text

    def print_other_insts(self):
        text = pd.DataFrame(columns=['Назва', 'Тип', 'Тип оплати', 'Ціна', 'Заборгованість', 'Специфікація', 'id'])
        for element in self.table_of_other_insts:
            text.loc[element.id] = element.values()
        return text

    def print_all(self):
        text = pd.DataFrame(columns=['Назва', 'Тип', 'Тип оплати', 'Ціна', 'Заборгованість', 'Специфікація', 'id'])
        for element in self.table:
            text.loc[element.id] = element.values()
        return text
