my_dict = {"one": "один",
           "two": "два",
           "three": "три",
           "four": "чотири",
           "five": "п'ять",
           "six": "шість",
           "seven": "сім",
           "eight": "вісім",
           "nine": "дев'ять",
           "ten": "десять"}
with open("data.txt", encoding='utf-8') as data:
    list_of_data = data.read().split()

print(list_of_data)

translated_data = [my_dict.get(word, word) for word in list_of_data]

print(translated_data)

with open("data_ua.txt", "w") as out:
    out.write(" ".join(translated_data))
