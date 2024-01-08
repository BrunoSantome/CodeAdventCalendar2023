
import re



numbers = ['one','two','three','four','five','six','seven','eigh','nine']
numbers2 = ['twone','oneigh']

dict = {'one':"1",'two':"2",'three':"3",'four':"4",'five':"5",'six':"6",'seven':"7",'eigh':"8",'nine':"9"}
dict2 = {'twone':'21','oneigh':'18'}
file = open("file.txt",'r')
#file = ['46threethreevqs8114','fivek1five','onesix7onefive9','qqptcnrxlllvccssrkkmkxnz8','3sxfscfseventhree','four86six6']

file_list_numbers =[]
file_list_numbers2 =[]
file_list = []

for line in file:
    file_list.extend(line.split())


for i in file_list:
    for num in numbers2:
        if num in i:
            i = i.replace(num,dict2[num])
    file_list_numbers2.append(i)
    
for i in file_list_numbers2:
    for num in numbers:
        if num in i:
            i = i.replace(num,dict[num])
    file_list_numbers.append(i)


file_list_numbers_letters = []

for i in file_list_numbers:
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


