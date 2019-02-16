import random

def play():
    print("****************************")
    print("Welcome to the game Diviner.")
    print("****************************")

    secret_number = random.randrange(1, 101)
    try_number = 0
    points = 1000

    level = int(input("Choose a difficulty ---> (1) Easy || (2) Normal || (3) Hard: "))

    if(level == 1):
        try_number = 10
    elif(level == 2):
        try_number = 7
    elif(level == 3):
        try_number = 3

    for round_number in range(1, try_number + 1):
        print("Try {} of {} tries".format(round_number, try_number))
        kick_str = input("Enter your number between 1 and 100: ")
        print("Your kick", kick_str)
        kick = int(kick_str)

        if(kick < 1 or kick > 100):
            print("Please, choice a number between 1 and 100.")
            continue

        hit = kick == secret_number
        bigger = kick > secret_number
        small = kick < secret_number

        if (secret_number == kick):
            print("You're right! Make {} points".format(points))
            break
        else:
            if(bigger):
                print("You missed. His kick was bigger than the secret number.")
            elif(small):
                print("You missed. His kick was less than the secret number.")
            
            failures = abs(secret_number - kick)
            points = points - failures

    print("End of the game.")

if(__name__ == "__main__"):
    play()