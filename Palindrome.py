

word = "cac"
def palindrome_1():
    for x in range(len(word)):
        if word[x] == word[-x]:
            print(word[x])
            print('okay')
        else:
            print('not okay')


def palindrome():
    a = int(len(word)/2)
    for x in range(a):
        if word[x] != word[(len(word)-x-1)]:
            return print("False")

    return print("true")

def GuessNumber():
    number = str(1905)
    guess = str(input("Guess the 4 digit number: "))
    a = 0
    b = 0
    while a != 4:
        for x in range(len(number)):
            if guess[x] == number[x]:
                a += 1
            number = list(number)
            if guess[x] in number:
                b += 1
        if a != 4:
            print("You have " + str(b) + " numbers that are in the answer")
            print("You have " + str(a) + " numbers in the right spot")
            a = 0
            b = 0
            guess = str(input("Guess the 4 digit number: "))

    print("You guessed the right number!")

def ArrayGame():
    array = [2, 1, 4, 3]
    list1 = 0
    k = 1
    for x in range(len(array)):
        for y in range(len(array)):
            if array[x] - array[y] == k:
                list1 += 1
    print(list1)

ArrayGame()

def Merge_Sort():
    list1 = [2,3,5,4]



question = 'given an "array" with positive number, your task is to find the largest subset from array that contains elementst tat are fibonnaci'
example = "[1,4,9,7,10,13]"
