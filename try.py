import csv
import MySQLdb

mydb= MySQLdb.connect(host='localhost',
    user='root',
    db='celebal')
cursor=mydb.cursor()

with open('dataset1.csv', 'r') as csvfile:
	csv_data1 = csv.reader(csvfile, delimiter=',')
	next(csv_data1)
	cursor.execute("TRUNCATE TABLE data1")
	for row in csv_data1:
		cursor.execute("INSERT INTO data1(ID,Cities,Pincode,Office_ID) VALUES(%s,%s,%s,%s)",row)
	mydb.commit()
with open('dataset2.csv','r') as csvfile2:
	csv_data2 = csv.reader(csvfile2,delimiter=',')
	next(csv_data2)
	cursor.execute("TRUNCATE TABLE data2")
	for row in csv_data2:
		cursor.execute("INSERT INTO data2(ID,Office_ID,Population) VALUES(%s,%s,%s)",row)
	mydb.commit()
cursor.execute("DROP TABLE new_records")
sql=("CREATE TABLE new_records AS SELECT d.ID,d.Office_ID,d.Cities,d.Pincode,dd.population from data1 d join data2 dd on d.Office_ID=dd.Office_ID;")
cursor.execute(sql)
cursor.close()
print("Done")
