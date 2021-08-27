MAX_NUM = 15
nums_gen = (el for el in range(1, MAX_NUM + 1, 2))
print(*nums_gen)
print(type(nums_gen))