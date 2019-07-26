'''
11.	Following are the initials of players who play various games. Some of these players play more than one game.
Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football: [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]

Write a program to:
a.	List those players who play all three games.
b.	List those players who play exactly one game.

'''
Cricket = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton = [ "PKM", "ALN", "NV", "KM","RMV"]

d = {}
allThree =[]
onlyOne = []
lst = [Cricket,Football,Badminton]
for j in lst:
    for i in j:
        if d.get(i) != None:
            d[i] += 1
        else:
            d[i] = 1
for key in d:
    if d[key] == 3:
        allThree.append(key)
    if d[key] == 1:
        onlyOne.append(key)
print(f"All 3 Games: {allThree}")
print(f"Only 1 Games: {onlyOne}")
