
def part1():
    h = int(input('Please enter the height of the triangle: '))
    outside_outline = (input('Please enter a symbol for the triangle outline: '))
    inside = input('Please enter a symbol for the triangle fill: ')

    for a in range(h):
        if h < 4:
            print(str((outside_outline) * h))
            h -= 1


    for a in range(h):
        if h >= 4:
            print(str(outside_outline * h))
            while h >= 4:
                h -= 1
                print(str(outside_outline) + str(inside*(h-2)) + str(outside_outline))
                if h <= 3:
                    print(str(outside_outline*2))
                    print(str(outside_outline))

def part2():
    x = 1
    superpowerslist = []
    while x != 0:
        a = input("Please enter a superpower or type 'QUIT' to stop: ")

        if a == 'QUIT':
            break
        elif a not in superpowerslist:
            superpowerslist.append(a)
        elif a in superpowerslist:
            print('You already have that power!')
            dic = list(dict.fromkeys(superpowerslist))

    amount = 0
    if len(superpowerslist) == 0:
        ammount = 0
    elif len(superpowerslist) >= 1:
        amount = len(superpowerslist)

    print('You have ' + str(amount) + ' superpowers')
    if amount == 3:
        print('You are a perfect superhero!')
    elif amount > 3:
        print('You are too powerful!')
    else:
        print('You are underpowered!')

def part3():
    x = 1
    while x != 0:
        a = input('Please enter a password: ')

        if any(c.islower() for c in a) == False:
             print('Your password must contain a lowercase letter!')
        elif any(c.isupper() for c in a) == False:
             print('Your password must contain an uppercase letter!')
        elif len(a) < 6:
            print('Your password must be at least 6 letters!')
        elif len(a) > 20:
            print("Your password can't be longer than 20 letters!")
        elif len(a) >= 6 and len(a) <= 13 and '7' not in a:
            print('If your password is between 6 and 13 characters it must include a 7!')
        elif len(a) >= 14 and len(a) <= 20 and '2' not in a:
            print('If your password is between 14 and 20 characters it must include a 2')
        elif '0' in a and 'O' in a:
            print('Your password can not contain an O and a 0 at the same time! (uppercase o)')
        else:
            break

    print('Thank you for choosing the secure password: ' + str(a))

def part4():
    x = 4
    list1 = []
    list2 = []
    while x != 5:
        y = input('Please enter and item, or type END to stop ')
        if y != 'END':
            list1.append(y)
            z = input('Please enter the amount you would like to purchase ')
            list2.append(z)
        else:
            break

    total = 0

    print('Here is your grocery list')
    for a in range(len(list1)):
        print('Purchase ' + list1[a] + ' of ' + list2[a])
    for b in range(0, len(list2)):
        total = total + int(list2[b])

    print('Your total purchase is ' + str(total) + ' items')

def part5():
    wordslist = []
    for x in range(11):
        y = input('please enter a word: ')
        if y not in wordslist:
            wordslist.append(y)
        elif y in wordslist:
            print('you have already entered this word, please enter a different one')
            dic = list(dict.fromkeys(wordslist))
        else:
            continue

    print('')

    for a in range(len(wordslist)):
        if 'pre' in wordslist[a]:
            b = len(wordslist[a])
            without_pre = str(wordslist[a])
            print('You should ' + without_pre[3:b] + ' early.')
        elif 'post' in wordslist[a]:
            b = len(wordslist[a])
            without_post = str(wordslist[a])
            print('You should ' + without_post[4:b] + ' later.')
        else:
            word = str(wordslist[a])
            print('You can ' + word + ' whenever!')

def checkCapitalLetter(x):
    a = len(x)
    for b in range(a):
        if x[b] == x[b].isupper():
            print('Hi')
part1()