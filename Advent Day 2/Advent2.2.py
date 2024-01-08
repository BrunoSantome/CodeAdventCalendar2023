
file = open("file.txt",'r')
whole_list =   []
Rounds_list = []

dictLimit = {'blue':14,'red':12,'green':13}

for line in file:
    
    whole_list.append(line.split(":"))

whole_list_clean=[]
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

    return {'blue':int(blueCounter),'red':int(redCounter),'green':int(greenCounter)}



Possible_game_list = []
for game in clean_Rounds_list_2:
    game_N = []
    
    MinGameNumbers = {}
    for round in game:
        GameNumbers = retrieveNumbers(round)
           
        if not MinGameNumbers:
            MinGameNumbers = GameNumbers
        else:
            if GameNumbers['blue'] > MinGameNumbers['blue']:
                MinGameNumbers['blue'] = GameNumbers['blue']
            if GameNumbers['red'] > MinGameNumbers['red']:
                MinGameNumbers['red'] = GameNumbers['red']
            if GameNumbers['green'] > MinGameNumbers['green']:
                MinGameNumbers['green'] = GameNumbers['green']                       
   
    
    Possible_game_list.append((MinGameNumbers['blue']*MinGameNumbers['red']*MinGameNumbers['green']))
    
counter = 0
for a in Possible_game_list:
    counter+=a
print(counter)