'''This program shows the number between 1500 and 2000 divisible by 7 and multiple of 5'''

for num in range(1500,2001):
    if num%7==0 and num%5==0: #Check divisibility by 7 and 5
        print(num,end=",")