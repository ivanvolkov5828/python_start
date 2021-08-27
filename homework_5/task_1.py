def nums_generate(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums_gen = nums_generate(15)
print(*nums_gen)
print(type(nums_gen))
