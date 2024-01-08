file = open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day3\\input.txt', 'r')

Content = []

for line in file:
    Content.append(list(line))

for c in Content:
    for d in c:
        if d == '\n':
            c.remove(d)

matrix = []
for c in Content: 
    Content_clean = []
    a=""
    for d in c: 
        if d == '.':
            a = d.replace(d, 'X')
            Content_clean.append(a)
        if d.isdigit():
            a = d.replace(d, d)
            Content_clean.append(a)
        elif d != '.' and not d.isdigit(): 
            a = d.replace(d, 'S')
            Content_clean.append(a)
    matrix.append(Content_clean)


def check(matrix, row, column):

    #Si son esquina de la matriz
    if row == 0 and column == 0:
       if matrix[row+1][column] == 'S' or matrix[row][column+1] == 'S' or matrix[row+1][column+1] == 'S':
           return True 
       else:
           return False
    elif row == 0 and column == len(matrix)-1:
       if matrix[row+1][column] == 'S' or matrix[row][column-1] == 'S' or matrix[row-1][column-1] == 'S':
           return True
       else:
           return False
    elif row == len(matrix)-1 and column == 0:
        if matrix[row][column+1] == 'S' or matrix[row-1][column] == 'S' or matrix[row-1][column] == 'S':
           return True
        else:
            return False
    elif row == len(matrix)-1 and column == len(matrix)-1:
        if matrix[row][column-1] == 'S' or matrix[row-1][column] == 'S' or matrix[row-1][column-1] == 'S':
           return True

    #Si estan en las paredes de la matriz.
    elif row == 0 and column != len(matrix)-1:
        if matrix[row][column-1] == 'S' or matrix[row+1][column-1] == 'S' or matrix[row+1][column] == 'S' or matrix[row+1][column+1] == 'S' or matrix[row][column+1] == 'S':
            return True
        else:
            return False

    elif row == len(matrix)-1 and column != 0:
        if matrix[row][column-1] == 'S' or matrix[row-1][column-1] == 'S' or matrix[row-1][column] == 'S' or matrix[row-1][column+1] == 'S' or matrix[row][column+1] == 'S':
            return True
        else:
            return False
    elif row != len(matrix)-1 and column == 0:
        if matrix[row-1][column] == 'S' or matrix[row-1][column+1] == 'S' or matrix[row][column+1] == 'S' or matrix[row+1][column+1] == 'S' or matrix[row+1][column] == 'S':
            return True
        else:
            return False

    elif row != len(matrix)-1 and column == len(matrix)-1:
        if matrix[row-1][column] == 'S' or matrix[row-1][column-1] == 'S' or matrix[row][column-1] == 'S' or matrix[row+1][column-1] == 'S' or matrix[row+1][column] == 'S':
            return True
        else:
            return False
    elif row != len(matrix)-1 and column != len(matrix)-1 and row != 0 and column != 0:
        if matrix[row-1][column-1] == 'S' or matrix[row-1][column] == 'S' or matrix[row-1][column+1] == 'S' or matrix[row][column+1] == 'S' or matrix[row+1][column+1] == 'S' or matrix[row+1][column] == 'S' or matrix[row+1][column-1] == 'S' or matrix[row][column-1] == 'S':
            return True
        else:
            return False


List_digits = []
add = 0
for row in range(0, len(matrix)):
    for column in range(0, len(matrix)):
        if (add > 0):
            add = add - 1
            continue   
        lastdigit = ""
        SimbolAround = False
        add = 0
        if matrix[row][column].isdigit():
            lastdigit = f'{matrix[row][column]}'
            if check(matrix, row, column):
                SimbolAround = True
            if column+1 <= len(matrix)-1 and matrix[row][column+1].isdigit():
                lastdigit = f'{matrix[row][column]}{matrix[row][column+1]}'  
                if check(matrix, row, column+1):
                    SimbolAround = True
                add = 1
                if column+2 <= len(matrix)-1 and matrix[row][column+2].isdigit():
                    lastdigit = f'{matrix[row][column]}{matrix[row][column+1]}{matrix[row][column+2]}'
                    if check(matrix, row, column+2):
                        SimbolAround = True
                    add = 2

        if SimbolAround:
            List_digits.append(lastdigit)     
counter = 0
for i in List_digits:
    counter += int(i)

print(counter)
