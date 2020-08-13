import csv



# Getting data as a list of string -------------------------------
with open('employee.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",", escapechar='\\')

    line_cnt = 0


    for row in csv_reader:
        print(csv_reader.line_num, ':', row)

        if line_cnt == 0:       # Header
            print(f"Columns: {','.join(row)}")
        else:
            print(f"Data:  {row[0]} - {row[1]} - {row[2]} - {row[3]} ")
        
        line_cnt += 1

print('-----------------------------------------------------------')
# Getting data as a dictionary -------------------------------
with open('employee.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter="," , escapechar='\\')

    line_cnt = 0

    for row in csv_reader:
        print(csv_reader.line_num, row)

        if line_cnt == 0:       # Header
            print(f"Columns: {','.join(row)}")
            line_cnt += 1
        
        print(f"Data:  {row['empid']} - {row['name']} - {row['department']} - {row['salary']} ")
        line_cnt += 1

    print('-----------------------------------------------------------')