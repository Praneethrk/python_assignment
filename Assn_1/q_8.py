'''
8.	Write a program to accept 2 numbers “m” and “n” from the user; determine the value of mn without using predefined functions.
'''
m = int(input("Enter m : "))
n  = int(input("Enter n : "))
res = 1
if n > 0:
    for i in range(0, n):
        res *= m
print(res)