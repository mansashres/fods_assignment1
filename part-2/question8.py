'''This program create a number guessing game for the user'''
import random

answer = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess the correct number between 1 and 100")

attempts =5
#Check if the guess is correct,too high,or too low
for i in range (attempts):

 guess =int(input(f"Attempt{i+1}: Enter your guess:"))

 if guess==answer:
    print("Congratulations! you guessed the correct number!")
    break #Exit the loop since the correct number is guessed
 elif guess<answer:
   print("Too low! Try again.")
 else:
   print("Too high! Try again.")
 if i == attempts-1:
   print(f"Game Over! The correct number was{answer}.")

