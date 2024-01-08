


#Advent code day 1

file_list = []

file = open("file.txt",'r')

for line in file:
    file_list.extend(line.split())

file_list_numbers_letters = []
for i in file_list:
    file_list_numbers_letters.append(list(i))

file_list_numbers_only = []

for i in file_list_numbers_letters:
    numb = []
    for j in i:
        if j.isdigit():
            numb.append(j)
    file_list_numbers_only.append(numb)

final_list = []

for i in file_list_numbers_only:
    n = []
    if len(i) > 1:
        n.append(f'{i[0]}{i[-1]}')
    elif len(i) == 1:
        n.append(f'{i[0]}{i[0]}')
    final_list.append(n)

total_number = 0

for i in final_list:
    for j in i:
        total_number += int(j)

print(total_number)