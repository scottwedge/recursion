#!/usr/bin/env python3

# Sum of the digits in a number

val = 874321

# With recursion:
def add_digits(n, sum):
    if n > 0:
        digit = n % 10
        sum = sum + digit
        remainder = n // 10
        return add_digits(remainder, sum)
    else:
        return sum

result = add_digits(val, 0)
print("Recursive result= ", result)


# Without recursion
num = val
sum = 0
while num > 0:  
    right_most_digit = num % 10
    sum = sum + right_most_digit
    num = num // 10
    
print ("Sum of digits is {}".format(sum))
