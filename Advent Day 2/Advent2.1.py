
file = open("file.txt",'r')
whole_list =   []
Rounds_list = []

dictLimit = {'blue':14,'red':12,'green':13}

for line in file:
    
    whole_list.append(line.split(":"))

whole_list_clean=[]
print(whole_list)
for c in whole_list:
    whole_list_clean.append([c[1]])


for w in whole_list_clean:
    Rounds_list.extend([w[0].split(";")]) 


clean_Rounds_list = []    
for c in Rounds_list:
    lista = []
    for b in c:
        d = b.replace(' ','')
        lista.append(d.replace('\n',''))
    clean_Rounds_list.append(lista)

clean_Rounds_list_2 = []
for i in clean_Rounds_list:
    lista = []
    for c in i:
        lista.append(c.split(','))
    clean_Rounds_list_2.append(lista)

def retrieveNumbers(game):
    
    blueCounter = ''
    redCounter = ''
    greenCounter = ''
    for c in game:
        if 'blue' in c:
            for i in range(0,(len(c)-len('blue'))):
                if blueCounter == '':
                    blueCounter = c[i]
                else:
                    blueCounter = f'{blueCounter[0]}{c[i]}'
        if 'red' in c: 
            for i in range(0,(len(c)-len('red'))):
                if redCounter == '':
                    redCounter = c[i]
                else:
                    redCounter = f'{redCounter[0]}{c[i]}'
        if 'green' in c: 
            for i in range(0,(len(c)-len('green'))):
                if greenCounter == '':
                    greenCounter = c[i]
                else:
                    greenCounter= f'{greenCounter[0]}{c[i]}'
    
    if redCounter == '':
        redCounter = 0
    if greenCounter == '':
        greenCounter = 0
    if blueCounter == '':
        blueCounter = 0

    return {'blue':blueCounter,'red':redCounter,'green':greenCounter}
#Part1
def checkPossibleGame(Numbers, limit):
    checks = 0
    if int(Numbers['blue']) <= limit['blue']:
        checks+=1
    if int(Numbers['green']) <= limit['green']:
        checks += 1
    if int(Numbers['red']) <= limit['red']:
        checks += 1
    
    if checks == 3:
        return True
    else:
        return False

Total_possible_games=[]

for game in clean_Rounds_list_2:
    game_N = []
    Possible_game_list = []
    for round in game:
        GameNumbers = retrieveNumbers(round)
        if checkPossibleGame(GameNumbers,dictLimit):
            Possible_game_list.append(True)
        elif not checkPossibleGame(GameNumbers,dictLimit):
            Possible_game_list.append(False)

    if False in Possible_game_list:
        Total_possible_games.append(False)
    else:
        Total_possible_games.append(True)

counter = 0
for i in range(1,len(Total_possible_games)+1):
    if Total_possible_games[i-1] == True:
        counter+=i

print(counter)