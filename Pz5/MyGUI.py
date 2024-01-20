from tkinter import *
import tkinter as tk
from tkinter import ttk
from Institution import Club, School, Kindergarten, OtherInst


class GUI:
    def __init__(self, insts):
        self.win = Tk()
        self.menu = Menu(self.win)
        self.page = "all"
        self.insts = insts

    def win_conf(self):
        self.win.title('Заклади')
        self.win.state('zoomed')
        self.win.geometry("1680x960+0+0")
        photo = tk.PhotoImage(file='icon.png')
        self.win.iconphoto(False, photo)
        self.win.config(bg="lightgray")

    def menu_conf(self):
        self.win.config(menu=self.menu)
        self.menu.add_command(label="Весь список", command=self.all)
        self.menu.add_command(label="Школа", command=self.schools)
        self.menu.add_command(label="Садочки", command=self.kindergartens)
        self.menu.add_command(label="Гуртки", command=self.clubs)
        self.menu.add_command(label="Інше", command=self.other_insts)

    def start(self):
        self.win_conf()
        self.menu_conf()
        self.set_top()
        self.set_table()
        self.entry()
        self.set_buttons()
        self.all()
        self.win.mainloop()

    def set_top(self):
        top_title = Label(self.win,
                          text="Навчальні заклади",
                          font=("Times new Roman", 24),
                          bg="#81E688",
                          foreground="black")
        top_title.pack(side=TOP, fill=X)
        self.top = Frame(self.win, bg="lightgray")
        self.top.pack(pady=20, padx=40)

    def set_table(self):
        info = Frame(self.top, bg='#98FFE1')
        info.pack(side=TOP)
        scroll = Scrollbar(info)
        scroll.pack(side=RIGHT, fill=Y)
        self.treeview = ttk.Treeview(info,
                                     columns=("Назва", "Тип", "Тип оплати", "Ціна", "Заборгованість", "Спеціальність"),
                                     yscrollcommand=scroll.set, height=20, show='headings')
        self.treeview.heading("Назва", text="Назва")
        self.treeview.heading("Тип", text="Тип")
        self.treeview.heading("Тип оплати", text="Тип оплати")
        self.treeview.heading("Ціна", text="Ціна")
        self.treeview.heading("Заборгованість", text="Забогоргованість")
        self.treeview.heading("Спеціальність", text="Спеціальність")
        self.treeview.tag_configure("oddrow", background="white")
        self.treeview.tag_configure("evenrow", background="#81E688")
        scroll.config(command=self.treeview.yview)
        self.treeview.pack(side=LEFT)

    def set_buttons(self):
        self.buttons = LabelFrame(self.top,
                                  font=("Times new Roman", 15),
                                  bg="lightgray",
                                  foreground="black")
        self.buttons.pack(side=BOTTOM)
        self.button_pay = tk.Button(self.buttons,
                                    text="Оплатити",
                                    bg="#81E688",
                                    font=('Times New Roman', 14),
                                    relief=RAISED,
                                    command=self.pay_selected_item)
        self.button_edit = tk.Button(self.buttons,
                                     text="Редагувати",
                                     bg="#81E688",
                                     font=('Times New Roman', 14),
                                     relief=RAISED,
                                     command=self.edit_selected_item)
        self.button_delete = tk.Button(self.buttons,
                                       text="Видалити",
                                       bg="#81E688",
                                       font=('Times New Roman', 14),
                                       relief=RAISED,
                                       command=self.delete_selected_item)
        self.button_create = tk.Button(self.buttons,
                                       text="Додати",
                                       bg="#81E688",
                                       font=('Times New Roman', 14),
                                       relief=RAISED,
                                       command=self.create_item)
        self.button_day = tk.Button(self.buttons,
                                    text="Пропустити день",
                                    bg="#81E688",
                                    font=('Times New Roman', 14),
                                    relief=RAISED,
                                    command=self.skip_day)
        self.button_week = tk.Button(self.buttons,
                                     text="Пропустити тиждень",
                                     bg="#81E688",
                                     font=('Times New Roman', 14),
                                     relief=RAISED,
                                     command=self.skip_week)
        self.button_pay.grid(row=0, column=0, padx=10, stick="ew")
        self.button_edit.grid(row=0, column=1, padx=10, stick="ew")
        self.button_delete.grid(row=0, column=2, padx=10, stick="ew")
        self.button_create.grid(row=0, column=3, padx=10, stick="ew")
        self.button_day.grid(row=1, column=0, columnspan=2, padx=10, pady=10, stick="ew")
        self.button_week.grid(row=1, column=2, columnspan=3, padx=10, pady=10, stick="ew")

    def entry(self):
        adv_frame = LabelFrame(self.top,
                               text="Дані",
                               font=("Times new Roman", 15),
                               bg="lightgray",
                               foreground="black",
                               relief=tk.GROOVE)
        adv_frame.pack(pady=20, padx=20)

        name_label = tk.Label(
            adv_frame,
            text="Назва:",
            bg="lightgray",
            foreground="black",
            font=("Times new Roman", 14),
            padx=10
        )
        name_label.grid(row=0, column=0, stick='w', pady=10)
        self.name_entry = tk.Entry(
            adv_frame,
            bd=1,
            bg="white",
            font=("Times new Roman", 12),
            foreground="black"
        )
        self.name_entry.grid(row=0, column=1, stick='ew', padx=15)

        type_label = tk.Label(
            adv_frame,
            text="Тип:",
            bg="lightgray",
            foreground="black",
            font=("Times new Roman", 14),
            padx=10
        )
        type_label.grid(row=0, column=2, stick='w', pady=10)
        self.type_entry = ttk.Combobox(
            adv_frame,
            state="readonly",
            foreground="black",
            font=("Times new Roman", 13)
        )
        self.type_entry["values"] = ("", "Школа", "Дитячий садок", "Гурток", "Інше")
        self.type_entry.grid(row=0, column=3, stick='ew', padx=15)

        payment_label = tk.Label(
            adv_frame,
            text="Тип оплати:",
            bg="lightgray",
            foreground="black",
            font=("Times new Roman", 14),
            padx=10
        )
        payment_label.grid(row=0, column=4, stick='w', pady=10)
        self.payment_entry = ttk.Combobox(
            adv_frame,
            state="readonly",
            foreground="black",
            font=("Times new Roman", 13)
        )
        self.payment_entry["values"] = ("", "Денна", "Тижнева", "Місячна", "Річна")
        self.payment_entry.grid(row=0, column=5, stick='ew', padx=15)

        price_label = tk.Label(
            adv_frame,
            text="Ціна:",
            bg="lightgray",
            foreground="black",
            font=("Times new Roman", 14),
            padx=10
        )
        price_label.grid(row=1, column=0, stick='w', pady=10)
        self.price_entry = tk.Entry(
            adv_frame,
            bd=1,
            bg="white",
            foreground="black",
            font=("Times new Roman", 13)
        )
        self.price_entry.grid(row=1, column=1, stick='ew', padx=15)

        debt_label = tk.Label(
            adv_frame,
            text="Заборгованість:",
            bg="lightgray",
            foreground="black",
            font=("Times new Roman", 14),
            padx=10
        )
        debt_label.grid(row=1, column=2, stick='w', pady=10)
        self.debt_entry = tk.Entry(
            adv_frame,
            bd=1,
            bg="white",
            foreground="black",
            font=("Times new Roman", 13)
        )
        self.debt_entry.grid(row=1, column=3, stick='ew', padx=15)

        spec_label = tk.Label(
            adv_frame,
            text="Спеціальність:",
            bg="lightgray",
            foreground="black",
            font=("Times new Roman", 14),
            padx=10
        )
        spec_label.grid(row=1, column=4, stick='w', pady=10)
        self.spec_entry = tk.Entry(
            adv_frame,
            bd=1,
            bg="white",
            foreground="black",
            font=("Times new Roman", 13)
        )
        self.spec_entry.grid(row=1, column=5, stick='ew', padx=15)

    def clear_entry(self):
        self.name_entry.delete(0, "end")
        self.type_entry.set("")
        self.price_entry.delete(0, "end")
        self.payment_entry.set("")
        self.debt_entry.delete(0, "end")
        self.spec_entry.delete(0, "end")

    def create_item(self):
        spec = "-"
        try:
            name = str(self.name_entry.get())
            price = float(self.price_entry.get())
            inst_type = str(self.type_entry.get())
            payment = str(self.payment_entry.get())
            try:
                spec = str(self.spec_entry.get())
            except (RuntimeError, TypeError, ValueError):
                pass
            try:
                debt = int(self.debt_entry.get())
                match inst_type:
                    case "Школа":
                        self.insts.add_inst(School(name, price, payment, len(self.insts.table), debt))
                    case "Гурток":
                        self.insts.add_inst(Club(name, price, payment, len(self.insts.table), spec, debt))
                    case "Дитячий садок":
                        self.insts.add_inst(Kindergarten(name, price, payment, len(self.insts.table), debt))
                    case "Інше":
                        self.insts.add_inst(OtherInst(name, price, payment, len(self.insts.table), spec, debt))
            except (RuntimeError, TypeError, ValueError):
                match inst_type:
                    case "Школа":
                        self.insts.add_inst(School(name, price, payment, len(self.insts.table)))
                    case "Гурток":
                        self.insts.add_inst(Club(name, price, payment, len(self.insts.table), spec))
                    case "Дитячий садок":
                        self.insts.add_inst(Kindergarten(name, price, payment, len(self.insts.table)))
                    case "Інше":
                        self.insts.add_inst(OtherInst(name, price, payment, len(self.insts.table), spec))
        except (RuntimeError, TypeError, ValueError):
            pass
        self.update_table()
        self.clear_entry()

    def delete_selected_item(self):
        selected_items = self.treeview.selection()
        for item in selected_items:
            self.treeview.delete(item)
            self.insts.delete_inst(int(item))
        self.update_table()
        self.upgrade_table()

    def pay_selected_item(self):
        selected_items = self.treeview.selection()
        for item in selected_items:
            self.insts.pay(int(item))
        self.update_table()

    def edit_selected_item(self):
        selected_items = self.treeview.selection()
        self.edit_name(selected_items)
        self.edit_type(selected_items)
        self.edit_price(selected_items)
        self.edit_payment(selected_items)
        self.edit_debt(selected_items)
        self.edit_specification(selected_items)
        self.update_table()
        self.clear_entry()

    def edit_name(self, selected_items):
        name = str(self.name_entry.get())
        if name:
            for item in selected_items:
                self.insts.edit_name(int(item), name)

    def edit_type(self, selected_items):
        inst_type = str(self.type_entry.get())
        if type:
            for item in selected_items:
                self.insts.edit_type(int(item), inst_type)

    def edit_price(self, selected_items):
        try:
            price = float(self.price_entry.get())
            for item in selected_items:
                self.insts.edit_price(int(item), price)
        except (RuntimeError, TypeError, ValueError):
            pass

    def edit_debt(self, selected_items):
        try:
            debt = float(self.debt_entry.get())
            for item in selected_items:
                self.insts.edit_debt(int(item), debt)
        except (RuntimeError, TypeError, ValueError):
            pass

    def edit_payment(self, selected_items):
        payment = str(self.payment_entry.get())
        if payment:
            for item in selected_items:
                self.insts.edit_payment(int(item), payment)

    def edit_specification(self, selected_items):
        spec = str(self.spec_entry.get())
        if spec:
            for item in selected_items:
                self.insts.edit_spec(int(item), spec)

    def skip_day(self):
        self.insts.skip_day()
        self.update_table()

    def skip_week(self):
        self.insts.skip_week()
        self.update_table()

    def all(self):
        self.clear_table()
        tex = self.insts.print_all()
        self.fill_table(tex)
        self.upgrade_table()
        self.page = "all"

    def clubs(self):
        self.clear_table()
        tex = self.insts.print_clubs()
        self.fill_table(tex)
        self.upgrade_table()
        self.page = "clubs"

    def schools(self):
        self.clear_table()
        tex = self.insts.print_schools()
        self.fill_table(tex)
        self.upgrade_table()
        self.page = "schools"

    def kindergartens(self):
        self.clear_table()
        tex = self.insts.print_kindergartens()
        self.fill_table(tex)
        self.upgrade_table()
        self.page = "kinder"

    def other_insts(self):
        self.clear_table()
        tex = self.insts.print_other_insts()
        self.fill_table(tex)
        self.upgrade_table()
        self.page = "other"

    def clear_table(self):
        self.treeview.delete(*self.treeview.get_children())

    def fill_table(self, tex):
        for index, row in tex.iterrows():
            values = (row["Назва"], row["Тип"], row["Тип оплати"], row["Ціна"], row["Заборгованість"], row["Специфікація"])
            if index % 2 == 0:
                self.treeview.insert("", tk.END, values=values, iid=row["id"], tags='evenrow')
            else:
                self.treeview.insert("", tk.END, values=values, iid=row["id"], tags='oddrow')
        self.treeview.pack()

    def upgrade_table(self):
        for i, item in enumerate(self.treeview.get_children()):
            if i % 2 == 0:
                self.treeview.item(item, tags='evenrow')
            else:
                self.treeview.item(item, tags='oddrow')

    def update_table(self):
        match self.page:
            case "all":
                self.all()
            case "clubs":
                self.clubs()
            case "schools":
                self.schools()
            case "kinder":
                self.kindergartens()
            case "other":
                self.other_insts()
