from flask import Flask
import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='celebal')
app = Flask(__name__) 
cursor=mydb.cursor()
@app.route('/')   
def main():
    cursor.execute("select sum(population) as num, Pincode from new_records where Cities='Jaipur' group by Pincode;")	
    result=cursor.fetchall()
    return str(result)

if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run(port=8000)  
