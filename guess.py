import random
secret_number = random.randrange(0,10)
print("A secret random number has been generated!")
guessed = False
while guessed==False:
    user_input = int(input("Try to guess: "))
    if user_input==secret_number:
        guessed = True
        print("You guessed it!")
    elif user_input < 0 or user_input  >= 10 :
        print("The secret number is between 0 and 10!")
    elif user_input > secret_number:
        print("Try one more time, a bit lower")
    elif user_input < secret_number:
        print("Try one more time, a bit higher")

print("Game over!")
