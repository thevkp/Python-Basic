import random

rand_value = random.randint(1,10)

# if guess == rand_value:
#     print("You guessed it right.")
# else:
#     print("Wrong Guess")

chance = 5
guess = int(input("What's your guess: "))
chance -= 1
while chance > 0:
    if guess > rand_value:
        print("Too high. Try a smaller number.")
    elif guess < rand_value:
        print("Too low. Try a greater number.")
    elif guess == rand_value:
        print("Correct guess.")
        break

    guess = int(input((f"Chances left: {chance}\nMake a new guess: ")))
    chance -= 1

if chance == 0 and guess != rand_value:
    print(f'Game over. The correct number was {rand_value}.')


