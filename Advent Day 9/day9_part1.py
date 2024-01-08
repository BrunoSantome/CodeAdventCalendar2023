with open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day9\\input.txt', 'r') as f:
    data= f.read().split('\n')

def findPattern(line):
    sequences = [line]
    while not all(v == 0 for v in sequences[-1]):
        nextSequence = []
        for i in range(0, len(line)):
            if i != len(line)-1:   
                nextSequence.append(line[i+1]-line[i])
        line = nextSequence
        sequences.append(nextSequence)
    last_val = 0
    for i, value in enumerate(sorted(sequences, key=len)):

        if i != len(sequences):
            last_val += value[-1]
    return last_val
        
sum = 0
for line in data:
    list_line = line.split(' ')
    line_int = [eval(i) for i in list_line]
    sum += findPattern(line_int)
print(sum)
