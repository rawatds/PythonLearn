import pandas

df = pandas.read_csv('hrdata.csv')
print(df)
#print(type(df['Hire Date'][0]))    # <class 'str'>
print('------------------------------------')


df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)
#print(type(df['Hire Date'][0]))     # #print(type(df['Hire Date'][0]))
print('------------------------------------')


df = pandas.read_csv('hrdata.csv', index_col='Employee', parse_dates=['DOJ'], header=0, names=['Employee', 'DOJ', 'Salary', 'Leave Balance'])
print(df)

df.to_csv('hrdata_modified.csv')

print("Done")
