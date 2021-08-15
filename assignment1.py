"""
Replace the contents of this module docstring with your own details
Name:
Date started:
GitHub URL:
"""
import random


def displayMenu():
    """
    display a menu for the user to choose from [2, 3]
    """
    print('Menu:')
    print('L - List places')
    print('R - Recommend random place')
    print('A - Add new place')
    print('M - Mark a place as visited')
    print('Q - Quit')


def displayPlaceList(placeList):
    countNotVisit = 0
    placeListLen = len(placeList)
    visitList = []
    notVisitList = []
    # traverse the placeList
    for i in range(len(placeList)):
        place = placeList[i]
        # has visit
        if place[3] == 'v':
            visitList.append(place)
        # not has visit
        if place[3] == 'n':
            countNotVisit += 1
            notVisitList.append(place)
    visitList.sort(key=lambda x: x[2])
    notVisitList.sort(key=lambda x: x[2])
    # not has visit
    for i in range(len(notVisitList)):
        place = notVisitList[i]
        print('*{}. {:<15}in {:<15}{:>3}'.format(i + 1, place[0], place[1], place[2], place[3]))
    # has visit
    for i in range(len(visitList)):
        place = visitList[i]
        print(' {}. {:<15}in {:<15}{:>3}'.format(len(notVisitList) + i + 1, place[0], place[1], place[2], place[3]))
    if countNotVisit !=0:
        print('{} places. You still want to visit {} places.'.format(placeListLen, countNotVisit))
    else:
        print('{} places. No places left to visit. Why not add a new place?'.format(placeListLen))
    return notVisitList + visitList


def recommend(placeList):
    print('Not sure where to visit next?')
    recommendList = []
    for i in range(len(placeList)):
        place = placeList[i]
        # not has visit
        if place[3] == 'n':
            recommendList.append(place)
    # random choose an unvisited place
    recommendPlace = random.choice(recommendList)
    print('How about... {} in {}?'.format(recommendPlace[0], recommendPlace[1]))


# You should be able to use generic, customisable functions to perform input with error checking
# (e.g., getting the place name and country can reuse the same function).
def getInputNameOrCountry(hint):
    while (True):
        result = input(hint + ': ')
        # blank
        if (result == ''):
            print('Input can not be blank')
        else:
            return result


def countUnVisit(placeList):
    countUnVisitNum = 0
    # print(placeList)
    # No unvisited places
    for place in placeList:
        if place[3] == 'n':
            countUnVisitNum += 1
    return countUnVisitNum


# You should be able to use generic, customisable functions to perform input with
# error checking (e.g., getting the place name and country can reuse the same function).
def main():
    # display a welcome message with your name in it
    print("Travel Tracker 1.0 - by Xu Yezhou")
    # initial the place list
    placeList = []

    # load a CSV (Comma Separated Values) file of places (just once at the very start);
    with open('places.csv') as f:
        line = f.readline().strip()
        # read line
        while (line):
            name = line.split(',')[0]
            country = line.split(',')[1]
            priority = int(line.split(',')[2])
            hasVisit = line.split(',')[3]
            placeList.append([name, country, priority, hasVisit])
            line = f.readline().strip()
    # length of the placeList
    placeListLen = len(placeList)
    print('{} places loaded from places.csv'.format(placeListLen))

    while True:
        displayMenu()
        choice = input('>>> ').upper()
        # error-check user inputs as demonstrated in the sample output [4]
        if choice not in ['L', 'R', 'A', 'M', 'Q']:
            print('Invalid menu choice')
        else:
            # quit the system
            # when the user chooses quit: save the places to the CSV file, overwriting the file contents
            # (note that this should be the only time that the file is saved)
            if choice == 'Q':
                with open('places.csv', mode='w') as f:
                    for place in placeList:
                        f.write(','.join([place[0], place[1], str(place[2]), place[3]]) + '\n')
                print('{} places saved to places.csv\nHave a nice day :)'.format(len(placeList)))
                break
            # recommend place
            if choice == 'R':
                countUnVisitNum = countUnVisit(placeList)
                if countUnVisitNum == 0:
                    print('No places left to visit!')
                else:
                    recommend(placeList)
            # add place
            if choice == 'A':
                name = getInputNameOrCountry('Name')
                country = getInputNameOrCountry('Country')
                priority = int(input('Priority: '))
                print('{} in {} (priority {}) added to Travel Tracker'.format(name, country, priority))
                placeList.append([name, country, priority, 'n'])
            # list the place
            if (choice == 'L'):
                placeList = displayPlaceList(placeList)
            # mark the place
            if (choice == 'M'):
                # count unVisit num
                countUnVisitNum = countUnVisit(placeList)
                # No unvisited places left
                if countUnVisitNum == 0:
                    print('No unvisited places')
                else:
                    # display the place list
                    placeList = displayPlaceList(placeList)
                    print('Enter the number of a place to mark as visited')
                    while True:
                        try:
                            n = int(input('>>> '))
                            # invalid input
                            if n <= 0:
                                print('Number must be > 0')
                            elif n > len(placeList):
                                print('Invalid place number')
                            # already visited
                            elif (placeList[n - 1][3] == 'v'):
                                print('You have already visited {}'.format(placeList[n - 1][0]))
                                break
                            else:
                                placeList[n - 1][3] = 'v'
                                print('{} in {} visited!'.format(placeList[n - 1][0], placeList[n - 1][1]))
                                break
                        # not a number
                        except ValueError as e:
                            print('Invalid input; enter a valid number')


if __name__ == '__main__':
    main()
