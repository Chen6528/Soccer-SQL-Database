import tkinter as tk
from tkinter import ttk
import pandas as pd
import getpass
from functions import *

user = getpass.getpass(prompt='User: ')
password = getpass.getpass(prompt='Password: ')

connection = connect_to_database(user, password, "localhost", "player_info")
cursor = connection.cursor()






testing_input = input("1: highest: ->")
if (testing_input == '1'):
    query = ''' 
            SELECT player_name, age, nation, team, market_value 
            FROM player_stats 
            ORDER BY market_value DESC 
            LIMIT 100
            '''
else:
    query = ''' 
            SELECT player_name, age, nation, team, market_value 
            FROM player_stats 
            LIMIT 100
            '''
cursor.execute(query)
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=['player_name', 'age', 'nation', 'team', 'market_value'])
players = df[['player_name', 'age', 'nation', 'team', 'market_value']]



root = tk.Tk()
root.title("Soccer Player Database")
root.geometry("800x600+100+100")

main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


tree = ttk.Treeview(main_frame, yscrollcommand=scrollbar.set, columns=('Name', 'Age', 'Nation', 'Team', 'Value'), show='headings')
tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

tree.heading('Name', text='Name')
tree.heading('Age', text='Age')
tree.heading('Nation', text='Nation')
tree.heading('Team', text='Team')
tree.heading('Value', text='Value')

tree.column('Name', width=200)
tree.column('Age', width=50)
tree.column('Nation', width=100)
tree.column('Team', width=200)
tree.column('Value', width=100)

for index, row in df.iterrows():
    tree.insert('', tk.END, values=(row['player_name'], row['age'], row['nation'], row['team'], row['market_value']))


root.mainloop()

cursor.close()
connection.close()