import mysql.connector
import pandas as pd
import getpass

user = getpass.getpass(prompt='User: ')
password = getpass.getpass(prompt='Password: ')

connection = mysql.connector.connect(
    user=user,
    password=password,
    host="localhost",
    database="test_import"
    )
cursor = connection.cursor()

query = ''' 
        
        '''

cursor.execute(query)