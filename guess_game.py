import random

number = random.randint(1, 20)
tries = 0
max_tries = 5

print("Welcome to the random number  random guess game!")

while tries < max_tries:
    num = int(input("Guess a number between 1 and 20: "))
    tries += 1

    if num < number: 
        print("")
        print("Too low!!! Try again.")
        print("")

    elif num > number:
        print("")
        print("Too high!! Try again.")
        print("")
        
    else:
        print("")
        print("Congratulations! You guessed the number in", tries, "tries!")
        print("")
        break
else:
    print("")
    print("Sorry, you used all your tries. The number was:", number, "")
