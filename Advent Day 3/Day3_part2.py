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
    a = ""
    for d in c:
        if d.isdigit():
            a = d.replace(d, d)
            Content_clean.append(a)
        if d == '*':
            a = d.replace(d, 'S')
            Content_clean.append(a)
        elif d != '*' and not d.isdigit(): 
            a = d.replace(d, 'X')
            Content_clean.append(a)
    matrix.append(Content_clean)


def SeeFullNumber(row,column,matrix):

    if column != 0 and column  != len(matrix)-1: 
        if matrix[row][column-1] == 'X' and matrix[row][column+1] == 'X':
            return matrix[row][column]
       
        elif matrix[row][column-1].isdigit() and matrix[row][column+1].isdigit():
            return f'{matrix[row][column-1]}{matrix[row][column]}{matrix[row][column+1]}'
        
        elif matrix[row][column-1].isdigit():  
            if matrix[row][column-2].isdigit():
                return f'{matrix[row][column-2]}{matrix[row][column-1]}{matrix[row][column]}'
            else:
                return f'{matrix[row][column-1]}{matrix[row][column]}'
        
        elif matrix[row][column+1].isdigit():
            if matrix[row][column+2].isdigit():
                return f'{matrix[row][column]}{matrix[row][column+1]}{matrix[row][column+2]}'
            else:
                return f'{matrix[row][column]}{matrix[row][column+1]}'
        else:
            return f'{matrix[row][column]}'


def isNumber(row, column, matrix):
    ListNumbers = []
    if matrix[row-1][column-1].isdigit():
        Number =  SeeFullNumber(row-1,column-1,matrix)
        if int(Number) not in ListNumbers:
            ListNumbers.append(int(Number))
    
    if matrix[row-1][column].isdigit():
        Number =  SeeFullNumber(row-1,column,matrix)
        if int(Number) not in ListNumbers:
            ListNumbers.append(int(Number))
        
    if matrix[row-1][column+1].isdigit(): 
        Number =  SeeFullNumber(row-1,column+1,matrix)
        if int(Number) not in ListNumbers:
            ListNumbers.append(int(Number))
    
    if matrix[row][column+1].isdigit():
        Number =  SeeFullNumber(row,column+1,matrix) 
        if int(Number) not in ListNumbers:
            ListNumbers.append(int(Number))
    
    if matrix[row+1][column+1].isdigit():
        Number =  SeeFullNumber(row+1,column+1,matrix)
        if int(Number) not in ListNumbers:
            ListNumbers.append(int(Number))
    
    if matrix[row+1][column].isdigit():
        Number =  SeeFullNumber(row+1,column,matrix) 
        if  int(Number) not in ListNumbers:
            ListNumbers.append(int(Number))
    
    if matrix[row+1][column-1].isdigit():
        Number =  SeeFullNumber(row+1,column-1,matrix)  
        if int(Number) not in ListNumbers:
            ListNumbers.append(int(Number))
    
    if matrix[row][column-1].isdigit():
        Number =  SeeFullNumber(row,column-1,matrix)  
        if int(Number) not in ListNumbers:
            ListNumbers.append(int(Number))
    print(ListNumbers)
    return ListNumbers    
         
List = []
for row in range(0,len(matrix)):
    for column in range(0,len(matrix)):
        if matrix[row][column] == 'S':
            value = isNumber(row,column,matrix)
            if len(value) == 2:
                List.append(isNumber(row, column, matrix))

sumGears = 0
for i in range(0,len(List)):
    mul = List[i][0] * List[i][1]
    sumGears += mul

print(sumGears)


