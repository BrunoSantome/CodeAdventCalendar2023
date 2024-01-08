import math
from itertools import cycle

file = open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day8\\input.txt', 'r')

Content = []

for line in file:
    d = line.replace('\n', '')
    l = d.replace('(','')
    a = l.replace(')','')
    b = a.replace(' ','')
    Content.append(b)

Directions = list(Content[0])

Content.remove(Content[0])
Content.remove(Content[0])

clean_Content = []
for c in Content:
    clean_Content.append(c.split('='))

dictionary = dict()

start_nodes = []
finish_nodes = []

for c in clean_Content:
    if 'A' in c[0]:
        start_nodes.append(c[0])
    dictionary[c[0]] = c[1].split(',')
print(start_nodes)

steps = 0
cycles = []

#Fuerza bruta: while not all('Z' in item for item in start_nodes))

for node in start_nodes:
    for steps, d in enumerate(cycle(Directions), start=1):
        if d == 'L':
            node = dictionary[node][0]
        if d == 'R':
            node = dictionary[node][1]
        if node[2] == 'Z':
            cycles.append(steps)
            print(cycles)
            break

print(math.lcm(*cycles))
