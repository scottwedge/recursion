#!/usr/bin/env python3

# Practice recursion

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


n=4
result = fact(n)
print(result)
