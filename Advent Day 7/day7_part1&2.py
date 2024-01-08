
from collections import Counter

Content = open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day7\\input.txt', 'r')

Content_clean = []
games = {}
for line in Content:
    l = line.replace('\n','')
    Content_clean.append(l.split(" "))

#Add to dictionary
cards_only = []
for c in Content_clean:
    games[c[0]] = c[1]
    cards_only.append(c[0])

def getIndex(card, rank):
    ind = "23456789TJQKA"
    
    Mapindex = map(ind.index, card)
    List_index = []
    List_index.append(rank)
    for ch in Mapindex:
        List_index.append(ch)
    return List_index

def getIndex1(card, rank):
    ind = "J23456789TQKA"
    
    Mapindex = map(ind.index, card)
    List_index = []
    List_index.append(rank)
    for ch in Mapindex:
        List_index.append(ch)
    return List_index

def getRank(Counts):

    if Counts.count(5) == 1:
        return 7
    elif Counts.count(4) == 1:
        return 6
    elif Counts.count(3) == 1 and Counts.count(2) == 1: 
        return 5   
    elif Counts.count(3) == 1: 
        return 4
    elif Counts.count(2) == 2: 
        return 3
    elif Counts.count(2) == 1: 
        return 2
    elif Counts.count(1) == 5:
        return 1


#part1
List_ordered = []
for card in cards_only:  
    
    ranked_card = getIndex1(card, getRank(sorted(Counter(card).values())))
    ranked_card.append(int(games[card]))
    List_ordered.append(ranked_card)
List_ordered = sorted(List_ordered)
win = 0


for i in range(1, len(List_ordered)+1):
    win = win + (i * List_ordered[i-1][6])
print(win)

#Part 2
List_ordered2 = []
for card in cards_only:
    
    count_sorted = sorted(Counter(card))
    jokers = Counter(card).pop('J', 0)
    temporal_card = card
    if 'J' in count_sorted and jokers != 5:
        temporal_card = card.replace('J', '')
        
    if jokers != 5:
        count_sorted_clean = sorted(Counter(temporal_card).values())
        count_sorted_clean[-1] += jokers
    else:
        count_sorted_clean=sorted(Counter(temporal_card).values())

    ranked_card = getIndex1(card, getRank(count_sorted_clean))
    ranked_card.append(int(games[card]))

    List_ordered2.append(ranked_card)
    
List_ordered2 = sorted(List_ordered2)

win2=0

for i in range(1, len(List_ordered2)+1):
    win2 += (i * List_ordered2[i-1][6])

print(win2)
