'''This program calculates the number of letter and digits in the given string'''

user_input=input("Enter a string:")

#Initializing counters
letter_count=0
digit_count=0
 
for char in user_input:
    if char.isalpha(): #check if the character is letter
      letter_count+=1
    elif char.isdigit(): #check if the charcter is digit
      digit_count+=1

print(f"Number of letters:{letter_count}")
print(f"Number of digit:{digit_count}")
