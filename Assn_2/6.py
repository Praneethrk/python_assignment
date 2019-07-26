'''6.	Write a program to find the sum of the given elements of the list. (Hint: Use reduce method.) '''

from functools import reduce
data = input("Enter the numbers: ")
lst = data.split(",")
sum = reduce(lambda a, b: int(a)+int(b), lst)
print(sum)