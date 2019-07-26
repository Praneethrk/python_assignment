class Employee:
    def __init__(self, empno, empname, salary):
        self._empno = empno
        self._empname = empname
        self._salary = salary

    def cal_salary(self):
        pass
    
    def display(self):
        print(f"Employee Id : {self._empno} \nEmployee name : {self._empname}")
    
        
class PermanentEmployee(Employee):
    
    def __init__(self, empno, empname, salary, bonus):
        super().__init__(empno, empname, salary)
        self.bonus = bonus
        self.totalSalary = 0

    def cal_salary(self):
        self.totalSalary = self._salary + self.bonus

    def display(self):
        self.cal_salary()
        super().display()
        print(f"Salary : {self.totalSalary}")

class ContractEmployee(Employee):

    def __init__(self, empno, empname,daySal, daysWorked):
        super().__init__(empno, empname,None)
        self.daySal = daySal
        self.daysWorked = daysWorked

    def cal_salary(self):
        self.totalSalary = self.daySal * self.daysWorked

    def display(self):
        self.cal_salary()
        super().display()
        print(f"Salary : {self.totalSalary}")