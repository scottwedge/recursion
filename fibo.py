#!/usr/bin/env python3

# Fibonacci sequence using recursion

def fibo(l):
    if l[-1] < 20000:
        sum = l[-1] + l[-2]
        print("Sum= ",sum)
        l.append(sum)
        print(l)
        return fibo(l)
    else:
        return l


l = [0,1]

result = fibo(l)
print(result)


"""
fibo = [0, 1]  # Initialize sequence

l = 10

while len(fibo) < l:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)


while fibo[-1] < 1000000:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)
"""
