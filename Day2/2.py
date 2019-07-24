'''
2.	Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row
'''
given = [[0,1,2,3],[3,4,5,5],[6,7,8,8],[9,0,1,9]]
lst = []
rowMin = []
rowMax = []
colMin = []
colMax = []
for i in given:
    rowMin.append(min(i))
    rowMax.append(max(i))
    for j in i:
        lst.append(j)

trns = [[given[j][i] for j in range(len(given))]for i in range(len(given[0]))]
for i in trns:
    colMin.append(min(i))
    colMax.append(max(i))

print(f"Minimum value in an array : {min(lst)}")
print(f"Maximum value in an array : {max(lst)}")
print(f"Elements with Minimum values column-wise: {colMin}")
print(f"Elements with Maximum values column-wise: {colMax}")
print(f"Elements with Minimum values row-wise: {rowMin}")
print(f"Elements with Maximum values row-wise: {rowMax}")

