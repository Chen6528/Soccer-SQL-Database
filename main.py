import mysql.connector
import pandas as pd
import getpass
import tkinter as tk
from tkinter import ttk


user = getpass.getpass(prompt='User: ')
password = getpass.getpass(prompt='Password: ')

connection = mysql.connector.connect(
    user=user,
    password=password,
    host="localhost",
    database="player_info"
    )
cursor = connection.cursor()

query = ''' 
        SELECT player_name, age, nation, team, market_value 
        FROM player_stats 
        ORDER BY market_value DESC 
        LIMIT 100
        '''
cursor.execute(query)

rows = cursor.fetchall()

cursor.close()
connection.close()
df = pd.DataFrame(rows)


