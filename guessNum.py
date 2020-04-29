# number guessing game with C H E A T S !!!

import random as r

queue = []

print("The number is between 1 and 100. Enter 0 for hint.")


def alpha_hint(comp):
    less = r.randrange((comp - 20), comp - 2)
    more = r.randrange(comp + 2, (comp + 20))

    if (comp <= 20) or (comp == 80):
        print("Alpha hint unavailable")
    else:
        print("The number is between", less, "and", more)


def hint(comp, item, div):

    if item == 1:
        if (comp % 2) == 0:
            print("The number is even")

        else:
            print("The number is odd")

    elif item == 2:
        if len(div) > 0:
            print("The number is divisible by", r.choice(div))

        else:
            print("The number is a prime number")

def arithmetic(comp, item, div):

    if item == 1:
        first = r.randrange(1, comp)
        item = r.randrange(1,3)

        if item == 1:
            print(first, "+", comp-first)

        elif item == 2:
            print(comp-first, '+', first)

    elif item == 2:
        first = r.randrange(comp, 100)
        print(first, '-', abs(comp-first))

    elif item == 3:
        first = r.choice(div)
        print(first, '*', int(comp / first))

    elif item == 4:
        mult = r.randrange(1, 13)
        first = comp * mult
        print(first, '/', mult)


def playGame():
    global queue
    
    if len(queue) > 0:
        comp = queue[0]; queue.clear()

    else:
        comp = r.randrange(1, 101)

    # list of divisible numbers
    div = [i for i in range(2, comp) if comp % i == 0]

    while True:
        user = int(input("\nGuess Number: "))

        # if user guesses correct
        if user == comp:
            print("Correct, the answer was", comp)
            break
            
        # adds test number to queue
        elif user == 2020:
            nextNum = int(input("Add Test Number: "))

            if (nextNum >= 101) or (nextNum <= 0):
                print("Number must be within 1 and 100")

            else:
                queue.append(nextNum)

        # shows arithmetic problem
        elif user == 111:
            arithmetic(comp, r.randrange(1,5), div)

        # gives answer (super cheat)
        elif user == 910:
            print(comp)

        # shows list of divisible numbers
        elif user == -1:
            if len(div) == 0:
                print("Prime")
            else:
                print(*div, sep=', ')

        # shows number within a range
        elif user == 101:
            alpha_hint(comp)

        # shows if number even/odd OR divisible factors
        elif user == 0:
            hint(comp, r.randrange(1, 3), div)

        # if user is higher
        elif user > comp:
            print("Too high!")

        # if user is lower
        elif user < comp:
            print("Too low!")

    # play again
    again = input("\nPlay Again?(Y/N) ").upper()

    if again == 'Y':
        playGame()

    elif again == 'N':
        print("Thank you for playing!")
    
    else:
        print("Please follow directions. Goodbye.")

playGame()
