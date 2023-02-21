import csv

# open "EmployeePay" file to read
# call csv.reader to read "EmployeePay" file; name to employee_infile

# skip line 1 of employee_infile

# create for loop for employees_infile
# print first and last name
# print salary
# print bonus
# close "EmployeePay" file

employees = open("EmployeePay.csv", "r")

employee_infile = csv.reader(employees, delimiter=",")


for record in employee_infile:
    print("-------------------- Employee ", record[0], "------------------------")
    print(f"Name: {record[1]} {record[2]}")
    print(f"Salary: ${record[3]}")
    print(f"Bonus: {record[4]}")

employees.close()
