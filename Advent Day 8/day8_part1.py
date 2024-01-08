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

for c in clean_Content:
    dictionary[c[0]] = c[1].split(',')


finishValue = 'ZZZ'
currentValue = 'AAA'
steps = 0

while currentValue != finishValue: 
    for d in range(0, len(Directions)):
        nextInstruction = dictionary[currentValue]
        if Directions[d] == 'L':
            currentValue = nextInstruction[0]
        if Directions[d] == 'R':
            currentValue = nextInstruction[1]
        steps += 1
print(steps)
