# create variables
first_name = 'John'
last_name = 'Doe'


# create a full name variable by concatenating first and last name
full_name = first_name + " " +  last_name


# create a new variable to store address 
address = '123 Main Street' 

# Use the += operator to add the string , Apartment 4B to your address variable.
address += ', Apartment 4B'

# create age variable
employee_age = 28

# creating a variable employee_info assign it the result of concatenating: the full_name variable.
employee_info = full_name + " is " + str(employee_age) + " years old."   # convert employee_age to a string using str(employee_age)

# print employee_info
print(employee_info)

# Create a variable named experience_years and assign it the integer 5
experience_years = 5

#  create a variable experience_info. Assign it a string formed by concatenating 'Experience: ', the experience_years
experience_info = 'Experience: ' + str(experience_years) + ' years.'
print(experience_info)

# creating variables for postion and salary
position = 'Data Analyst'
salary = 75000

# Create a variable employee_card and assign it an f-string that displays Employee: followed by a space and the value of the full_name variable.
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'

# print employee_card
print(employee_card)

# create new vvariable for employee id
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]  # extract department from employee_code by slicing
print(department)

year_code = employee_code[4:8] # extract year from employee_code by slicing
initials = employee_code[9:11] # extract initial from employee_code by slicing
print(year_code)
print(initials)


last_three = employee_code[-3:] # extract employee_code number from employee_code by slicing
print(last_three)
