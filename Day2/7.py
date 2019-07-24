'''
7.	Write a program to find the sum of squares of only the even numbers in the given list.
 (Hint: Use the methods filter, map, reduce.)
'''
from functools import reduce
data = input("Enter the numbers: ")
lst = data.split(",")
even = list(filter(lambda x:int(x)%2 == 0,lst))
sq = list(map(lambda y:int(y) ** 2,even))
sum = reduce(lambda a, b: int(a)+int(b), sq)
print(sum)