file = open('C:\\Users\\U68603\\AppData\\Roaming\\Bruno\\Learning\\AdventCalendar\\day4\\input.txt', 'r')
# part 1


def check(list1, list2):
    wincards_list = []
    givencards_list = [] 
    points = 0 
    for number in list1.split(" "):
        if number != '':
            wincards_list.append(number)
    for number in list2.split(" "):
        if number != '':
            givencards_list.append(number)
    for a in givencards_list:
        for b in wincards_list:
            if a == b:
                points += 1
    return points


Content = []
for line in file:
    Content.append(line.split(":"))

cards = []
for c in Content:
    cards.append(c[1].replace('\n', '').split('|'))

matching_numbers_list = []
for round in cards:
    matching_numbers_list.append(check(round[0],  round[1]))

total_points_counter = 0
for p in matching_numbers_list:
    total_points_counter += int(p)

# Part 2
cards_copies = [1] * len(matching_numbers_list)

for i in range (0,len(cards_copies)):  
    matching_numbers = matching_numbers_list[i]
    if i == 0:
        for a in range (i+1, i+matching_numbers+1): 
            cards_copies[i+a] += 1
    else: 
        for a in range (1, 1+ matching_numbers):
            cards_copies[i+a] += cards_copies[i]

total_cards_counter = 0
for p in cards_copies:
    total_cards_counter += p

print(total_cards_counter)
