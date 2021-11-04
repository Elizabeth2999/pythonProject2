import random

# r = random.randrange(-5, 11)
# generates the upper limit inclusive ,random.randint(0, 10)
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print('Please input a number that is higher than 0 next time')
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0,top_of_range)
# print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. ")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
            print("Oops!,Your guess is above the number!")
        else:
            print("Oops!,Your guess is below the number!")
print("Bravo!, you won with", guesses, "no of guesses.")