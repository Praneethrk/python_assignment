'''1.	Write a program to generate a fancy number for a new vehicle considering the following constraints:
a.	The fancy number should have 4-digits.
b.	The sum of these 4-digits should be 12.
c.	The 3rd digit should be equal to the difference between the 1st and the 2nd digit.
d.	The 4th digit should be equal to the sum of the 1st and the 3rd digit.

The program should be able to generate all the possible 4-digit numbers that meet the above listed criteria.
'''
def sumOf(num):
    sum = 0
    while num != 0:
        sum = sum + num % 10
        num = num // 10
    return sum == 12

def splitNo(num):
    temp = num
    temp, a = temp % 1000, temp //1000
    temp, b = temp % 100, temp //100
    temp, c = temp % 10, temp //10
    temp, d = temp % 1, temp //1
    return a,b,c,d

for i in range(1000,10000):
    if sumOf(i):    
        a, b, c, d = splitNo(i)
        if a - b == c and a + c ==d:
            print(i) 
