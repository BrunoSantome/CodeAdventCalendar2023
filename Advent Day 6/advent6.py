
def simulateRace(SpeedBoat,time, distance):
    totalTime = time-SpeedBoat
    totalDistance = 0
    if SpeedBoat == 0:
        return False
    if SpeedBoat != 0:
        totalDistance = SpeedBoat * totalTime
        if totalDistance > distance:
            return True
        elif totalDistance <= distance:
            return False

def calc(time, distance):
    winRate = 0
    for option in range(0,time+1):
        if simulateRace(option,time,distance):
            winRate += 1

    return winRate

if __name__ == "__main__":
    
    #PART 1
    time = [40,81,77,72]
    distance= [219,1012,1365,1089]

    ways = 1
    for i in range (0,len(time)):
        ways *= calc(time[i],distance[i])
    print(ways)

    #PART 2
    time2 = 40817772
    distance2 = 219101213651089

    print(calc(time2,distance2))