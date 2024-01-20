import csv
import matplotlib.pyplot as plt
import pandas as pd


# Функція для зчитування даних з файлу
def read_csv(file_path):
    data = pd.read_csv(file_path,
                       encoding="cp1251",
                       delimiter=";",
                       header=0,
                       index_col=0)
    return data


# Функція для додавання студента у файл
def add_student(file_path):
    with open(file_path, 'a',
              newline='',
              encoding="cp1251") as file:
        writer = csv.writer(file, delimiter=';')
        name = str(input("Ім'я:"))
        try:
            english = int(input("Англійська:"))
            data_base = int(input("БД:"))
            kpi = int(input("КПІ:"))
            kps = int(input("КПС:"))
            theory = int(input("ТЙ:"))
            physics = int(input("Фізика:"))
        except (TypeError, ValueError):
            print("Неправильно введено дані!")
            return
        writer.writerow([name, english, data_base, kpi, kps, theory, physics])


# Функція для видалення студента з файлу
def delete_student(file_path):
    data = read_csv(file_path)
    name = str(input("Ім'я:"))
    try:
        data.drop(name, inplace=True)
    except KeyError:
        print("Немає такого студента!")
        return
    data.to_csv(file_path, index=True, header=True, encoding="cp1251", sep=";")


# Функція для відображення статистики студента
def info_student(data):
    student = str(input("Ім'я:"))
    title = "Оцінки студента: " + student
    colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']
    plt.figure(figsize=(16, 10), dpi=80)
    try:
        bars = plt.bar(data.columns, data.loc[student], color=colors)
    except KeyError:
        print("Немає такого студента!")
        return
    plt.title(title, fontsize=24)
    plt.ylim(0, 110)
    plt.ylabel("Бал", fontsize=18)
    plt.xlabel("Предмет", fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    for bar, value in zip(bars, data.loc[student]):
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 1, str(value), fontsize=18)
    plt.show()


# Функція для відображення статистики по предмету
def info_subject(data):
    subject = str(input("Предмет:"))
    title = "Статистика: " + subject
    colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']
    plt.figure(figsize=(16, 10), dpi=80)
    try:
        bars = plt.bar(data.index, data[subject], color=colors)
    except KeyError:
        print("Немає такого предмета!")
        return
    plt.ylim(0, 110)
    plt.title(title, fontsize=24)
    plt.ylabel("Бал", fontsize=18)
    plt.xlabel("Ім'я студента", fontsize=18)
    plt.xticks(fontsize=16, rotation=10)
    plt.yticks(fontsize=16)
    for bar, value in zip(bars, data[subject]):
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 1, str(value), fontsize=18)
    plt.show()


# Меню
def menu():
    print("=========================================="
          "\n1 - Вивести статистику студента"
          "\n2 - Вивести статистику предмету"
          "\n3 - Додати студента"
          "\n4 - Видалити студента"
          "\n5 - Вийти"
          "\n==========================================")
    file_path = "table.csv"
    data = read_csv(file_path)
    while True:
        try:
            response = int(input("Що ви хочете зробити?:"))
        except ValueError:
            continue
        match response:
            case 1:
                info_student(data)
            case 2:
                info_subject(data)
            case 3:
                add_student(file_path)
                data = read_csv(file_path)
            case 4:
                delete_student(file_path)
                data = read_csv(file_path)
            case 5:
                print("Бувай!!!")
                return


menu()
