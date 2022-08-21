# Write a program to fetch a record via api

from flask import Flask , request, jsonify

# Write a program to insert a record in a sql table via api

app = Flask(__name__)
@app.route('/xyz/aswini',methods = ['GET','POST'])

def sql():

    if request.method==['POST']:
        import mysql.connector as connection

        mydb = connection.connect(host="localhost", database='api', user="root", passwd="1234", use_pure=True)

        print(mydb.is_connected())
        query = "Select * from product"
        cursor = mydb.cursor()
        cursor.execute(query)
        for result in cursor.fetchall():
            print(result)
if __name__=='__main__'  :
    app.run()