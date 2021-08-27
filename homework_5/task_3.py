tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'

]

my_list = []
idx = 0
my_tuple = (None,)
for el in zip(tutors, classes):
    print(el)
    idx += 1

if len(classes) < len(tutors):
    for i in range(idx, len(tutors)):
        my_list.append(tutors[i])
        print(*zip(my_list, my_tuple))
        my_list = []
