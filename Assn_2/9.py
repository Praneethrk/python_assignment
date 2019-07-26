''' 9.	Write a program to find the word(s) that occur maximum and minimum number of times in the given paragraph. 
Also, display those words next to their respective count.

'''
data = "Comprehensions are a feature of Python which I would really miss if I ever have to leave it. \
        Comprehensions are constructs that allow sequences to be built from other sequences.\
        Several types of comprehensions are supported in both Python 2 and Python 3."

d = {}
lst = data.split()
for i in lst:
    if d.get(i) != None:
        d[i] += 1
    else:
        d[i] = 1
for key in d:
        print(f"{key} : {d[key]}")
maxi = max(d, key=lambda key: d[key])
mini = min(d, key=lambda key: d[key])
print(f"maximum :-> {maxi} : {d[maxi]}")
print(f"Minimum :-> {mini} : {d[mini]}")