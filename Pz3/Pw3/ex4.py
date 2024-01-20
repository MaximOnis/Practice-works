import random


def get_random_tuple(a, b):
    random_numbers = tuple(random.randint(a, b) for _ in range(10))
    return random_numbers


first_tuple = get_random_tuple(-5, 0)
second_tuple = get_random_tuple(0, 5)
third_tuple = first_tuple + second_tuple
print(first_tuple)
print(first_tuple.count(0))
print(second_tuple)
print(second_tuple.count(0))
print(third_tuple)
print(third_tuple.count(0))
