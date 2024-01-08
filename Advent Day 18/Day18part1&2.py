from shapely.geometry import Polygon

with open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day18\\input.txt', 'r') as f:
    data = f.read().split('\n')


Directions = []
Directions_part2 = []
Hexa_part2 = []

for line in data:
    dir, num, color = line.split()
    Directions.append([dir, int(num)])
    Hexa_part2.append(color)

for line in Hexa_part2:
    dirN = int(int(line[-2]))
    if dirN == 0:
        N = 'R'
    if dirN == 1:
        N = 'D'
    if dirN == 2:
        N = 'L'
    if dirN == 3:
        N = 'U'

    Directions_part2.append([N, int(line[2:-2], 16)])

perimeter = 0
perimeter2 = 0

for a in Directions:
    perimeter += a[1]
for a in Directions_part2:
    perimeter2 += a[1]


def dig(Directions):
    position = (0, 0)
    Dig_List = [position]
    for value in Directions:
        if value[0] == 'R':
            position = (position[0], position[1]+value[1])
        elif value[0] == 'L':
            position = (position[0], position[1]-value[1])
        elif value[0] == 'U':
            position = (position[0]-value[1], position[1])
        elif value[0] == 'D':
            position = (position[0]+value[1], position[1])
        Dig_List.append((position))

    return Dig_List


Directions = dig(Directions)
polygon_part1 = Polygon(Directions)

Directions_part2 = dig(Directions_part2)
polygon_part2 = Polygon(Directions_part2)

"""
Code below to calculate the area without the library
sum = 0
for i in range(0,len(Directions)):
    if i != 0 and i != len(Directions)-1:
        sum += Directions[i][0]*(Directions[i+1][1]-Directions[i-1][1])
"""

sum = int(polygon_part1.area) - perimeter//2 + 1 
sum += perimeter

sum2 = int(polygon_part2.area) - perimeter2//2 + 1
sum2 += perimeter2

#print sum part1    
print(f'Part 1: {sum}')
print(f'Part 2: {sum2}')
