
with open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day15\\input.txt', 'r') as f:
    data = f.read().strip().split(',')

#part1

sum=0

for val in data:
    current_value = 0
    for i in val:
        current_value += ord(i)
        current_value = (current_value* 17)%256
    sum+=current_value
#print(sum)

def hash(val):
    current_value = 0
    for i in val:
        current_value += ord(i)
        current_value = (current_value* 17)% 256
    return current_value

#Cleaning of data

Final_ordered_list = []


data_striped =[]
for a in data:
    data_striped.append([*a])
Boxes = {}

for i in range(0, 255):
    Boxes[f'{i}'] = []

for value in data_striped:
    for a in value:
        substitution = False            
        if a == '=':
            number = value.pop()
            value.pop()
            for i, val in enumerate(Boxes[f'{hash("".join(value))}']):
                if val[0] == "".join(value):
                    val[1] = number
                    substitution = True
            if not substitution:
                Boxes[f'{hash("".join(value))}'].append(["".join(value), number])
        if a == '-':
            value.pop()
            for index, val in enumerate(Boxes[f'{hash("".join(value))}']):
                if val[0] == "".join(value):
                    Boxes[f'{hash("".join(value))}'].pop(index)
                else:
                    continue

Sum_solution = 0

for index1 in range(0,len(Boxes)):
    for index2 in range(0,len(Boxes[f'{index1}'])):
        Sum_solution += (int(index1)+1) * (int(index2)+1) * int(Boxes[f'{index1}'][index2][1])

print(Sum_solution)
