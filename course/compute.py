import json
courseLst = []
courses = {}
def add_course():
    courses['cid'] = int(input("Enter the couuse ID: "))
    courses['c_name'] = input("Enter the course name: ")
    courseLst.extend(courses)
    with open("course.json","a+",newline='') as f:
        json.dump(courseLst,f,indent=4)




add_course()