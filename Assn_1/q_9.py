'''
9.	Write a program to accept a five-digit number, increment each digit by 1 and then display the new number formed. 
Note that digit 9 gets incremented to 0.
'''
def split_number(num):
    digits = list()
    while num > 0:    
        digits.append(num % 10)
        num = num//10
    return digits

number = int(input("Enter a 5 digit number: "))
digits = split_number(number)
digits = digits[::-1]
res = 0

for digit in digits:
    if digit < 9:
        res = (res * 10) + (digit+1)
    else:
        res = (res * 10)

print(res)

    

 