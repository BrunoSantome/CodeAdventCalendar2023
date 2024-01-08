
import copy

with open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day14\\input.txt', 'r') as f:
    data = f.read().strip()

ws = [l.split() for l in data.split("\n")]

matrix = []

for a in ws:
    list=[]
    for c in a:
        for b in c:
            list.append(b)
    matrix.append(list)

def checkNorthPosition(matrix,row,column):
    if row == 0:
        return False
    
    elif row != 0:
        topvalue = matrix[row-1][column]      
        if topvalue == '.':
            return True
        if topvalue == '#':
            return False
        if topvalue == 'O':
            return False

matrix_update = matrix

End = False
while(not End):
    original_matrix = copy.deepcopy(matrix_update)
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix)):
            if matrix[row][column] == 'O':
                if checkNorthPosition(matrix, row, column):
                    matrix_update[row-1][column] = matrix[row][column]
                    matrix_update[row][column] = '.'
                else:
                    matrix_update[row][column] = matrix[row][column]
            else:
                matrix_update[row][column] = matrix[row][column]
    if original_matrix == matrix_update:
        End = True

rock_counter_row = []
for row in range(0, len(matrix)):
    counter = 0
    for column in range(0, len(matrix)):
        if matrix[row][column] == 'O':
            counter +=1
    rock_counter_row.append(counter)

sum_load = 0
for i in range(0, len(rock_counter_row)):  
    sum_load += rock_counter_row[i] * (len(rock_counter_row) - i)

print(sum_load)
