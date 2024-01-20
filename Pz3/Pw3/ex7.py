with open("nums.txt") as nums:
    list_of_nums = nums.read().split()

print(list_of_nums)

result = sum(int(word) for word in list_of_nums)
print(result)
