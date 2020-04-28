import random as r

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


def playGame():
    comp = r.randrange(1, 100)
    div = [i for i in range(2, comp) if comp % i == 0]

    while True:
        user = int(input("\nGuess Number: "))

        # if user guess correct
        if user == comp:
            print("Correct, the answer was", comp)
            break

        # gives answer (super cheat)
        elif user == 910:
            print(comp)

        # shows list of divisible numbers
        elif str(user) == '00':
            if len(div) == 0:
                print("Prime")
            else:
                print(*div, sep=', ')

        # shows number within a range
        elif user == 101:
            alpha_hint(comp)

        # shows if number even/odd OR divisible factors
        elif str(user) == 0:
            hint(comp, r.randrange(1, 3), div)

        # if user is higher
        elif user > comp:
            print("Too high!")

        # if user is lower
        elif user < comp:
            print("Too low!")

    again = input("\nPlay Again?(Y/N) ").upper()

    if again == 'Y':
        playGame()
    else:
        print("Thank you for playing!")


playGame()
