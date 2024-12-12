import random
print("Guess the number between 0 and 100")
random_number = random.randint(0, 100)
attempts = 1
print("You only have 5 attempts to guess the number")
while attempts <= 5:
    try:
        user_number = int(input("Guess the number: "))
        if user_number > 100:
            print("Enter a number less than 100")
            print(f"You only have {5 - attempts} left.")
            attempts += 1
            continue
        elif user_number > random_number:
            print("You,re number is higher than the random number.Please try again.")
            print(f"You have {5 - attempts} left.")
            attempts += 1
            continue
        elif user_number < 0:
            print("Enter a positive number.")
            print(f"You have {5 - attempts} left.")
            attempts += 1
            continue
        elif user_number < random_number:
            print("You've guessed lower than the actual number.Please try again")
            print(f"You only have {5 - attempts} left.")
            attempts += 1
            continue
        else:
            print("Congratulation you've guessed the number.")
            exit()
    except ValueError:
        print("Please enter a valid number")

print(f"You've lost the number was {random_number}")
