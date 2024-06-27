import tkinter as tk
from tkinter import ttk
import pandas as pd
import getpass
from functions import *

user = getpass.getpass(prompt='User: ')
password = getpass.getpass(prompt='Password: ')


connection = connect_to_database(user, password, "localhost", "player_info")
cursor = connection.cursor()

welcome = tk.Tk()
welcome.title("Welcome")
welcome.geometry("400x300+150+25")
descbutton = tk.Button(welcome, text="Sort by Decreasing Market Value", command=lambda:query_value_desc(cursor, welcome))
descbutton.pack(padx=20, pady=10)
incrbutton = tk.Button(welcome, text="Sort by Increasing Market Value", command=lambda:query_value_incr(cursor, welcome))
incrbutton.pack(padx=20, pady=10)
viewallbutton = tk.Button(welcome, text="View the Whole Database", command=lambda:query_normal(cursor, welcome))
viewallbutton.pack(padx=20, pady=10)
nationlabel = tk.Label(welcome, text="Search Players by Nation or Team", font=("Arial", 10))
nationlabel.pack(padx=20, pady=5)

input_entry = tk.Entry(welcome)
input_entry.pack(pady=2)
input_entry.bind('<Return>', lambda event: query_search(cursor, welcome, input_entry.get()))

inputbutton = tk.Button(welcome, text="Search", command=lambda: query_search(cursor, welcome, input_entry.get()))
inputbutton.pack(padx=20, pady=5)
welcome.mainloop()


rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=['player_name', 'age', 'nation', 'team', 'market_value'])
players = df[['player_name', 'age', 'nation', 'team', 'market_value']]



root = tk.Tk()
root.title("Soccer Player Database")
root.geometry("800x600+150+25")

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
    tree.insert('', tk.END, values=(row['player_name'], row['age'], row['nation'], row['team'], f"{row['market_value']} M"))


root.mainloop()
cursor.close()
connection.close()