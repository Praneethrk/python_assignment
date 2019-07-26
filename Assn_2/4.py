''' 4.	Write a program to accept an input string from the user and determine the vowels in the string and 
    calculate the number of vowels. (Hint: Use filter method.) '''
n = input("Enter your name: ")
lst = ['a', 'e', 'i', 'o', 'u']
res = list(filter(lambda y : y in lst, n))
print(f"{res} ; {len(res)}")