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

df = pd.DataFrame(rows, columns=['player_name', 'age', 'nation', 'team', 'market_value'])

top_players = df[['player_name', 'age', 'nation', 'team', 'market_value']]

root = tk.Tk()
root.title("Best Players")


frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Add a scrollbar to the frame
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a treeview widget
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=('Name', 'Age', 'Nation', 'Team', 'Value'), show='headings')
tree.pack(fill=tk.BOTH, expand=True)

# Configure the scrollbar
scrollbar.config(command=tree.yview)

# Define column headings
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')
tree.heading('Nation', text='Nation')
tree.heading('Team', text='Team')
tree.heading('Value', text='Value')

# Set column widths
tree.column('Name', width=200)
tree.column('Age', width=50)
tree.column('Nation', width=100)
tree.column('Team', width=200)
tree.column('Value', width=100)

# Insert data into the treeview
for index, row in top_players.iterrows():
    tree.insert('', tk.END, values=(row['player_name'], row['age'], row['nation'], row['team'], row['market_value']))

# Run the application
root.mainloop()
