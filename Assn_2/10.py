'''
10.	Write a program to count the number of unique words and 
the number of occurrences of each of those words from the question provided below.
'''
data = "How much wood would a woodchuck chuck if the woodchuck could chuck wood?"

d = {}
lst = data.split()
for i in lst:
    if d.get(i) != None:
        d[i] += 1
    else:
        d[i] = 1    
print(f"Number of unique word:{len(d)}")
print(d)