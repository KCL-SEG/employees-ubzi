"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_type, wage = 0, monthly_salary = 0, hours = 0, commission_type = None, commission_pay = 0, number_of_contracts = 0):
        self.name = name
        self.salary_type = salary_type
        self.commission_type = commission_type
        self.salary = self.modify_salary(monthly_salary, wage, hours)
        self.commission = self.modify_commission(commission_pay, number_of_contracts)

    def get_pay(self):
        return self.salary.calculate_pay() + self.commission.get_commission()

    def modify_salary(self, monthly_salary = 0, wage = 0, hours = 0):

        if (self.salary_type == "hourly"):
            salary = HourlySalary(wage = wage, hours = hours)
            return salary
        else:
            salary = MonthlySalary(monthly_salary)
            return salary

    def modify_commission(self, commission_pay = 0, number_of_contracts = 0):
        if (self.commission_type) == "Bonus":

            commission_object = Bonuscommission(commission_pay)

        elif (self.commission_type) == "Performance":

            commission_object = Performancecommission(commission_pay, number_of_contracts)

        else:
            commission_object = Nocommission(commission_pay)

        return commission_object

    def __str__(self):
        return f"{self.name} works on a {str(self.salary)}{str(self.commission)}.  Their total pay is {self.get_pay()}."


class Salary():
    pass

class HourlySalary(Salary):
    def __init__(self, hours, wage):
        self.hours = hours
        self.wage = wage

    def calculate_pay(self):
        return self.hours * self.wage

    def __str__(self):
        return f"contract of {self.hours} hours at {self.wage}/hour"

class MonthlySalary(Salary):
    def __init__(self, salary):
        #super().__init__(salary)
        self.salary = salary

    def calculate_pay(self):
        return self.salary

    def __str__(self):
        return f"monthly salary of {self.calculate_pay()}"

class commission:
    def __init__(self, commission_pay):
        self.commission_pay = commission_pay

class Bonuscommission(commission):
    def __init__(self, commission_pay):
        super().__init__(commission_pay)

    def get_commission(self):
        return self.commission_pay

    def __str__(self):
        return f" and receives a bonus commission of {self.commission_pay}"

class Performancecommission(commission):
    def __init__(self, commission_pay, number_of_contracts):
        self.number_of_contracts = number_of_contracts
        super().__init__(commission_pay)

    def get_commission(self):
        return self.commission_pay * self.number_of_contracts

    def __str__(self):
        return f" and receives a commission for {self.number_of_contracts} contract(s) at {self.commission_pay}/contract"

class Nocommission(commission):
    def __init__(self, commission_pay):
        super().__init__(commission_pay)

    def get_commission(self):
        return 0

    def __str__(self):
        return ""


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", monthly_salary = 4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', wage = 25, hours = 100)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', monthly_salary = 3000, commission_type = 'Performance', commission_pay = 200, number_of_contracts = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', wage = 25, hours = 150, commission_type = 'Performance', commission_pay = 220, number_of_contracts = 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', monthly_salary = 2000, commission_type = 'Bonus', commission_pay = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', wage = 30, hours = 120, commission_type = 'Bonus', commission_pay = 600)
