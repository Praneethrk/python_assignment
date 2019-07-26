'''
10.	Write a program to print the following output pattern.
         1
        121
       12321
      1234321
     123454321

'''
rows = int(input("Enter number of rows: "))
for i in range(1, rows+1):
    for j in range(1, rows+1-i):
        print(end=" ")
    for k in range(1, i):
        print(k, end="")
    for l in range(i, 0 ,-1):
        print(l, end="")
    print()
