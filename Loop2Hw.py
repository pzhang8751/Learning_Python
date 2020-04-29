import random

def part1():
    y = str(random.randint(1000, 10000))
    x = str(input('Guess a 4 digit number: '))
    print(y)
    cows = 0
    bulls = 0
    while x != y:
        for i in range(0, 4):
            if x[i] == y[i]:
                cows += 1
            elif x[i] in y:
                bulls += 1
        bull = bulls - cows
        print("you have %s cows and %d bulls" % (cows, bull))
        x = str(input('Guess a 4 digit number: '))

    print('You solved it!')
    return

def part2():
    size = int(input('How big do u want your board?'))
    a = 0
    while a < size:
        print(' ---' * size)
        print('|   ' * (size+1))
        a += 1
        if a >= size:
            print(' ---' * size)

def part3():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [x for x in a if x%2 == 0]
    print(b)

def part4():
    list1 = []
    x = 0
    answer = str(input('Name a number '))
    while x != 1:
        if answer != 'EXIT':
            list1.append(answer)
            answer = str(input('Name a number or type "EXIT" to stop '))
        elif answer == 'EXIT':
            list1.sort()
            number = str(input('Name another number '))
            if number in list1:
                print('true')
                x = 1
            elif number not in list1:
                print('False')
                x = 1

def part5():
    string = str(input('Type a word '))
    a = int(len(string)/2)
    b = len(string)
    list1 = []

    if b%2 == 0:
        for x in range(a):
            if string[x] == string[-x]:
                list1.append('true')
            elif string[x] != string[-x]:
                list1.append('false')
    elif b%2 == 1:
        for x in range(b):
            if string[x] == string[-x]:
                list1.append('true')
            elif string[x] != string[-x]:
                list1.append('false')

    if 'false' in list1:
        print('This string is not a palindrome')
    elif 'false' not in list1:
        print('This string is a palindrome')

part3()