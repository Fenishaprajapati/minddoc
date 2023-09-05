# install mysql
# pip install mysql
# pip install mysql-connector or
# pip install mysql-connector-python

import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234567890'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE Fenisha")

print("ALL DONE!")

# now go to the workbench and check the created database fenisha in the schema section(refresh it!!!)
