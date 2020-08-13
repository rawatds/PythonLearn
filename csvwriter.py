import csv


fieldnames = ['Name', 'Department', 'Salary']

# Using List
with open('emp_output.csv', 'w', newline='') as emp_file:

    emp_writer = csv.writer(emp_file, delimiter=',', quotechar='"', quoting = csv.QUOTE_NONE, escapechar='\\', )

    emp_writer.writerow(fieldnames);
    emp_writer.writerow(["Dharmender Rawat", "Java", 123.45])
    emp_writer.writerow(["Gupta, Savi", "Devops", 456])

# Using Dict
with open('emp_output2.csv', mode='w', newline='') as emp_file2:

    writer = csv.DictWriter(emp_file2, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"Department": "Java", 'Name': "Dharmender, Rawat",  "Salary": 123.45})
