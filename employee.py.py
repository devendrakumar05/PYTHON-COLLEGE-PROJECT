

# class Employee:
    
#     def __init__(self, name, age, salary):
        
        
#         self.name = name
#         self.age = age
#         self.salary = salary

#     #  the display method to display the details of the employee>>>>>>>>
#     def display(self):
#         # displaying the employee details>>>> 

#         print("Name:", self.name)       
#         print("Age:", self.age)
#         print("Salary:", self.salary)

#     # Define the increase_salary method to increase the salary of the employee>>>>>>>>>
#     def increase_salary(self, increase):
        
#         # salary increse function>>>>
#         self.salary += increase

# # Example >>>>>>>
# employee1 = Employee("DEVENDRA KUMAR", 30, 90000)
# employee1.display()

# employee2 = Employee("AKSAHT MITTAL", 35, 60000)
# employee2.display()

# # Increase salary 5000>>>>>>
# employee1.increase_salary(5000)
# employee1.display()

# # Increase the salary 2%>>>>>
# employee2.increase_salary(employee2.salary * 0.1)
# employee2.display()






# Employee Management System

class Employee:
    # Initialize the Employee object with a given name, age, and salary
    def __init__(self, name, age, salary):
        """
        Initialize the Employee object with a given name, age, and salary.

        :param name: The name of the employee.
        :param age: The age of the employee.
        :param salary: The salary of the employee.
        """
        self.name = name
        self.age = age
        self.salary = salary

    # Define the display method to display the details of the employee
    def display(self):
        """
        Display the details of the employee.

        :return: None
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

    # Define the increase_salary method to increase the salary of the employee
    def increase_salary(self, increase):
        """
        Increase the salary of the employee.

        :param increase: The amount to increase the salary by.
        :return: None
        """
        self.salary += increase

# Example usage:
employee1 = Employee("DEVENDRA KUMAR", 30, 90000)
employee1.display()

employee2 = Employee("AKSAHT MITTAL", 35, 60000)
employee2.display()

# Increase salary 5000
employee1.increase_salary(5000)
employee1.display()

# Increase the salary 2%
employee2.increase_salary(employee2.salary * 0.02)
employee2.display()

# Create a list of employees
employees = [employee1, employee2]

# Create a tuple of employees
employees_tuple = (employee1, employee2)






# Create a pandas DataFrame from the list of employees
import pandas as pd
employees_df = pd.DataFrame(employees)

# Print the list, tuple, and DataFrame
print("List of employees:")
print(employees)

print("\nTuple of employees:")
print(employees_tuple)

print("\nPandas DataFrame of employees:")
print(employees_df)