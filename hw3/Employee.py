class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def salary_raise(self, percent):
        self.salary *= (1 + percent / 100)

# instantiate
emp = Employee("John", 5000)

# increase salary by 10%
emp.salary_raise(10)

# print updated salary
print(emp.salary)
