import sqlite3

mydb=sqlite3.connect('hen.db')
mycursor=mydb.cursor()

mycursor.execute('SELECT * FROM emplo')
result = mycursor.fetchall()
print(result)

for row_num in range(len(result)):
	for col_num in range(4):
		data=result[row_num]
		print(data[col_num])
