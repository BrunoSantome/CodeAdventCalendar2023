with open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day21\\input.txt', 'r') as f:
    data = f.read().strip().split('\n')

matrix = []

for row in data:
    l = []
    for column in row:
        l.append(column)          
    matrix.append(l)

for row in range(0, len(matrix)):
    for column in range(0, len(matrix)):
        if matrix[row][column] == 'S':
            start_position = (row, column)

def check(position, matrix):
    row = position[0]
    column = position[1] 
    Result_List =[]
    if column != 0:
        if matrix[row][column-1] == '.' or matrix[row-1][column-1] == 'S':
            if (row,column-1) not in Result_List:
                Result_List.append((row, column-1))
    if column != len(matrix)-1:
        if matrix[row][column+1] == '.' or matrix[row][column+1] == 'S':
            if (row, column+1) not in Result_List:
                Result_List.append((row, column+1))
    if row != 0:
        if matrix[row-1][column] == '.' or matrix[row-1][column] == 'S' :
            if (row-1,column) not in Result_List:
                Result_List.append((row-1,column))
    if row != len(matrix)-1:
        if matrix[row+1][column] == '.' or matrix[row+1][column] == 'S':
            if (row+1,column) not in Result_List:
                Result_List.append((row+1, column))
    
    return Result_List

def checkDirections(start_position, matrix):
    Next_positions = []

    for p in start_position:
        
        Next_positions.extend(check(p, matrix))

    return Next_positions

steps = 0

List = checkDirections([start_position], matrix)

steps += 1
while steps != 64:
    List = list(dict.fromkeys(checkDirections(List, matrix)))    
    steps += 1

print(len(List))
