'''This program shows how to take two integer inputs from the user and display the result of the first number divided by the second'''
#Take two integer inputs from the user
num1=int(input("Enter the first interger:"))
num2=int(input("Enter the second interger"))

# Check if the divisor is not zero to avoid division error
if num2==0:
    print("Error ! Divison by zero is not allowed.")
else:
    result=num1/num2
    print(f"result:{result:.2f} ")  #Display result with 2 decimal places