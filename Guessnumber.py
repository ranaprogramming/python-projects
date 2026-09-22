# A Python command-line game where users try to guess a randomly generated number between 1 and 100. Includes high/low hints, attempt tracking, loops, conditionals, and user input handling.


import random

number = random.randint(1, 100)

attempts = 0  
print(number)

while True: 
    GuseNumber = int(input("Enter a number: "))

    attempts = attempts + 1
    
    if GuseNumber > number:
        print("Number is to high")
    elif GuseNumber < number:
        print("Number is to low")
    else:
        print(f"Congratulations you guessed the number: {number} ")
        print(f" Attempts: {attempts}")
        break