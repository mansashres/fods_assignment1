'''This program shows whether the number input is odd or even '''
# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
