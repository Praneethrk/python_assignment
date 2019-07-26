'''
4.	Make a class called Employee. It should be an abstract class with the following attributes and methods:

Attributes: 	empno, ename, salary
Methods: 	cal_salary() [abstract method]
display()  should display information empno, ename

Make a subclass of Employee with the name PermanentEmployee with the following attributes and methods:

Attributes: 	empno, ename, basic_salry, bouns
Methods:  	cal_salary() : [basic_salary + bouns]
display() should display information empno, ename, salary


Make another subclass of Employee with the name ContractEmployee with the following attributes and methods:

Attributes: 	empno, ename, day_sal, days_worked
Methods:  	cal_salary(): [day_sal * days_worked] 
display() should display information empno, ename, salary

Add at least 5 employees of different types and test the application.

'''


from employee import Employee , PermanentEmployee , ContractEmployee

if __name__ == "__main__":
    e1  = Employee('2001','Praneeth',1000000)
    e2 = PermanentEmployee('2002','Malya',100000,2000)
    e3 = ContractEmployee('2001','Joy',10000, 25)

    e1.display()
    e2.display()
    e3.display()