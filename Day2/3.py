'''
3.	Write a program to determine the work hours of the day entered based on the timetable provided below.

Mon	Tue	Wed	Thu	Fri	Sat	Sun
3	3	3	3	3	3	0
2	2	2	2	2	1	0
2	2	2	1	1	0	0

'''


lst = [[3,2,2],[3,2,2],[3,2,2],[3,2,1],[3,2,1],[3,1,0],[0,0,0]]
days = {'mon' : 0, 'teus' : 1, 'wed' : 2, 'thur' : 3, 'fri' : 4, 'sat' : 5, 'sun' : 6 }
day = input("Enter the day: ")
while True:
    if days.get(day) != None:
        print(lst[days.get(day)])
        break
    else:
        day = input("Enter the valid day: ")