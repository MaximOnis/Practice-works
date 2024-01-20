def reverse(input_dict):
    reversed_dict = {value: key for key, value in input_dict.items()}
    return reversed_dict

my_dict = {"DS-01": 12,
           "DS-02": 54,
           "DS-03": 22,
           "DS-04": 21,
           "DS-05": 32}
my_dict["DS-05"] = 16
my_dict["DS-11"] = 27
del my_dict["DS-03"]
print(my_dict)
print(reverse(my_dict))



