'''
1.	Make a class called Member. Create two attributes - first_name and last_name, and then create 5 more attributes that are typically stored in a Member profile, such as email, gender, contact_number, etc. Make a method called show_info() that prints a summary of the member’s information. Make another method called get_memeber() that prints personalized greetings to the member.

Create 5 instances representing different members and call both the methods for each member
'''


class Member:
    
    def __init__(self,fName,lName,email,gender,contact):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.gender = gender
        self.contact = contact

    def show_info(self):
        print(f"First Name : {self.fName}    Last Name : {self.lName}")
        print(f"Email : {self.email}")
        print(f"Gender : {self.gender}")
        print(f"Contact : {self.contact}")
        print()

    def get_member(self):
        print(f"Hello {self.fName} {self.lName} , Have a great day!!")
        print()

if __name__ == "__main__":
    M1 = Member('Praneeth','RK','praneethrk@gmail.com','Male','9587462130')
    M2 = Member('Joy','Dsouza','joydsouza@gmail.com','Male','8546213079')
    M3 = Member('Niranjan','Malya','kudureMalya@in.com','Male','8954623100')
    M4 = Member('Aishwarya','Rai Bachan','aishBachan@reddiffmail.com','Female','989989500')
    M5 = Member('Hrithik','Roshan','hrx@gmail.com','Male','985451304')

    M1.show_info()
    M1.get_member()
    M2.show_info()
    M2.get_member()
    M3.show_info()
    M3.get_member()
    M4.show_info()
    M4.get_member()
    M5.show_info()
    M5.get_member()