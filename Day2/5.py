'''5.	Write a program to add the elements of 2 arrays that are of the same dimension. (Hint: Use map method.) '''

in1 = input("Enter the 2 array of same dimentions:\n")
in2 = input()
lst1 = in1.split(",")
lst2 = in2.split(",")
print(list(map(lambda i,s: int(s) + int(i) , lst1,lst2)))