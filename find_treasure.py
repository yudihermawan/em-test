maxY = 6
maxX = 8
obstacles = [
    [3,3],
    [4,3],
    [5,3],
    [5,4],
    [7,4],
    [3,5],
]
treasureLocs = [
    [6,3],
    [7,3],
    [4,5]
]
triggerLocs = [
    [2,4,treasureLocs],
    [4,4,[
        treasureLocs[2]
    ]],
    [2,2,[
        treasureLocs[0],
        treasureLocs[1]
    ]],
    [6,2,[
        treasureLocs[0],
        treasureLocs[1]
    ]],
    [7,2,[
        treasureLocs[1]
    ]],
]
playerPositions = [
    [2,5]
]
navigationRules = [
    [1, 0, 0]
]
gotTreasure = 0

def is_coordinate_obstacle(x,y):
    for obstacle in obstacles:
        if x == obstacle[0] and y == obstacle[1]:
            return True
    return False

def is_wrong_step():
    currentPlayerPosition = playerPositions[len(playerPositions) - 1] 
    countNavigationRule = len(navigationRules)
    prevNavigationRule = navigationRules[countNavigationRule - 2]
    currentNavigationRule = navigationRules[countNavigationRule - 1]
    
    return currentPlayerPosition[0] == 1 or \
        currentPlayerPosition[1] == 1 or \
        currentPlayerPosition[0] == maxX or \
        currentPlayerPosition[1] == maxY or \
        is_coordinate_obstacle(currentPlayerPosition[0], currentPlayerPosition[1]) or \
        (prevNavigationRule[0] == 1 and prevNavigationRule[1] == 0 and currentNavigationRule[2] == 1) or \
        (prevNavigationRule[0] == 1 and prevNavigationRule[1] == 1 and prevNavigationRule[2] == 0 \
            and currentNavigationRule[0] == 1 and currentNavigationRule[1] == 0) or \
        (prevNavigationRule[0] == 1 and prevNavigationRule[1] == 1 and prevNavigationRule[2] == 1 \
            and currentNavigationRule[0] == 1 and currentNavigationRule[1] == 1)

def print_grid():
    print('')
    currentPlayerPosition = playerPositions[len(playerPositions) - 1]
    for y in range(1, maxY+1):
        for x in range(1, maxX+1):            
            if x == currentPlayerPosition[0] and y == currentPlayerPosition[1]:
                print('X', end= ' ')
            elif x == maxX:
                print('#')
            elif x == 1 or x == maxX or y == 1 or y == maxY or is_coordinate_obstacle(x,y):
                print('#', end= ' ')
            else: 
                print('.', end= ' ')

def print_possible_treasure():
    playerTriggered = playerPositions[len(playerPositions) - 1]
    for triggerLoc in triggerLocs:
        if playerTriggered[0] == triggerLoc[0] and playerTriggered[1] == triggerLoc[1]:
            print('\nPossible treasure location(s): ' + str(triggerLoc[2])) 
        

def find():
    print_grid()
    print('\nNavigation: ')
    print('A. Up/North')
    print('B. Right/East')
    print('C. Down/South')
    print('S. Stop')
    navigateTo = input('Choose navigation: ')
    print('------------------')

    prevPlayerPosition = playerPositions[len(playerPositions) - 1]
    if navigateTo == 'A' or navigateTo == 'a':
        playerPositions.append([prevPlayerPosition[0], prevPlayerPosition[1] - 1])
    elif navigateTo == 'B' or navigateTo == 'b':
        playerPositions.append([prevPlayerPosition[0] + 1, prevPlayerPosition[1]])
    elif navigateTo == 'C' or navigateTo == 'c':
        playerPositions.append([prevPlayerPosition[0], prevPlayerPosition[1] + 1])

    countPlayerPosition = len(playerPositions)
    if playerPositions[countPlayerPosition - 1][1] - playerPositions[countPlayerPosition - 2][1] == -1:
        navigationRules.append([1,0,0])
    elif playerPositions[countPlayerPosition - 1][0] - playerPositions[countPlayerPosition - 2][0] == 1:
        navigationRules.append([1,1,0])
    elif playerPositions[countPlayerPosition - 1][1] - playerPositions[countPlayerPosition - 2][1] == 1:
        navigationRules.append([1,1,1])

    if is_wrong_step():
        playerPositions.append(playerPositions[countPlayerPosition - 2])
        navigationRules.append(navigationRules[len(navigationRules) - 2])
        print('\nOops... wrong navigation!')

    print_possible_treasure()
    
    global gotTreasure
    if navigationRules[len(navigationRules) - 1][2] == 1:
        gotTreasure = gotTreasure + 1
        print('\nCongratulation.. You\'ve got ' + str(gotTreasure) + ' treasure(s)!')
        find()
    elif navigateTo == 'S' or navigateTo == 's':
        print('\nGoodbye...')
    else:
        find()

def main():
    find()

if __name__ == '__main__':
    main()