
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


def checkPosition(matrix,row,column,Position):

    if Position == 'N':
        if row == 0:
            return False
        else:
            row_ = row-1
            column_ = column
        
    if Position == 'W':
        if column == 0:
            return False
        else:
            row_ = row
            column_=column-1  

    if Position == 'S':
        if row == len(matrix)-1:
            return False
        else:
            row_ = row+1
            column_=column  
    if Position == 'E':
        if column == len(matrix)-1:
            return False
        else:
            row_ = row
            column_ = column+1

    topvalue = matrix[row_][column_]      
    if topvalue == '.':
        return True

def move_balls(End, matrix_update, matrix, Position):
    while (not End):
        original_matrix = copy.deepcopy(matrix_update)
        for row in range(0, len(matrix)):
            for column in range(0, len(matrix)):
                if matrix[row][column] == 'O':
                    if checkPosition(matrix, row, column, Position):
                        if Position == 'N':
                            matrix_update[row-1][column] = matrix[row][column]
                            matrix_update[row][column] = '.'
                        if Position == 'W':
                            matrix_update[row][column-1] = matrix[row][column]
                            matrix_update[row][column] = '.'
                        if Position == 'S':
                            matrix_update[row+1][column] = matrix[row][column]
                            matrix_update[row][column] = '.'
                        if Position == 'E':
                            matrix_update[row][column+1] = matrix[row][column]
                            matrix_update[row][column] = '.'
                    else:
                        matrix_update[row][column] = matrix[row][column]
                else:
                    matrix_update[row][column] = matrix[row][column]
        if original_matrix == matrix_update:
            End = True     
    return matrix_update


def getSum(matrix):
    rock_counter_row = []
    sum_load = 0
    
    for row in range(0, len(m)):
        counter = 0
        for column in range(0, len(m)):
            if m[row][column] == 'O':
                counter += 1
        rock_counter_row.append(counter)
    for i in range(0, len(rock_counter_row)):  
        sum_load += rock_counter_row[i] * (len(rock_counter_row) - i)
    return sum_load
    

Cycle = ['N','W','S','E']
matrix_update = matrix
Final_sum_List= []
End = False
index = 1

#De esta serie de números, se tardan 121 ciclos en colocar las bolas
#En la pososición 1000000000-121 = 999999879 empieza la serie
#La serie es:  79743, 79742, 79734, 79723, 79716, 79708, 79714, 79711, 79708, 79718, 79724, 79727, 79731, 79718, 79723, 79730, 79736, 79733
#La longitud de la serie es de 18
#Si dividimos 999999879 y obtenemos el resto de la división, nos sale 15. 
#La solución es la posición 15 de la serie, luego la solución es 79723

for i in range(0, 200):
    for dir in Cycle:
        m1 = []
        if i == 0 and dir == 'N':
            m = move_balls(End, matrix_update, matrix, dir)
        else:
            m = move_balls(End, m, m, dir)
    Final_sum_List.append(getSum(m))

    """
    if index%10 == 0:
        print(Final_sum_List)
        Final_sum_List = []
        index = 0
    index+=1
    """


