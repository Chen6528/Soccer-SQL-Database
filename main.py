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
center_window(welcome)

for i in range(20):
    welcome.grid_rowconfigure(i, weight=1)
welcome.grid_columnconfigure(0, weight=1)
welcome.grid_columnconfigure(1, weight=1)

introlabel = tk.Label(welcome, text="Welcome to the Soccer Database\nYou can view the database based on different sorting below", font=("Arial", 15))
introlabel.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

viewallbutton = tk.Button(welcome, text="View the Whole Database", command=lambda: query_normal(cursor, welcome))
viewallbutton.grid(row=2, column=0, columnspan=2, pady=10)

descbutton = tk.Button(welcome, text="Sort by Decreasing Market Value", command=lambda: query_value_desc(cursor, welcome))
descbutton.grid(row=3, column=0, padx=20, pady=10, sticky="e")

incrbutton = tk.Button(welcome, text="Sort by Increasing Market Value", command=lambda: query_value_incr(cursor, welcome))
incrbutton.grid(row=3, column=1, padx=20, pady=10, sticky="w")

nationlabel = tk.Label(welcome, text="Search Players by Nation/Team/Name/Position", font=("Arial", 10))
nationlabel.grid(row=4, column=0, columnspan=2, pady=5)

input_entry = tk.Entry(welcome)
input_entry.grid(row=5, column=0, columnspan=2, pady=2)

inputbutton = tk.Button(welcome, text="Search", command=lambda: query_search(cursor, welcome, input_entry.get()))
inputbutton.grid(row=6, column=0, columnspan=2, pady=5)
welcome.mainloop()


rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=['player_name', 'age', 'position', 'nation', 'team', 'market_value'])
players = df[['player_name', 'age', 'position', 'nation', 'team', 'market_value']]



root = tk.Tk()
root.title("Soccer Player Database")
root.geometry("800x600+150+25")

main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


tree = ttk.Treeview(main_frame, yscrollcommand=scrollbar.set, columns=('Name', 'Age', 'Position', 'Nation', 'Team', 'Value'), show='headings')
tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

tree.heading('Name', text='Name')
tree.heading('Age', text='Age')
tree.heading('Position', text='Position')
tree.heading('Nation', text='Nation')
tree.heading('Team', text='Team')
tree.heading('Value', text='Value')

tree.column('Name', width=200)
tree.column('Age', width=50)
tree.column('Position', width=150)
tree.column('Nation', width=100)
tree.column('Team', width=200)
tree.column('Value', width=100)

for index, row in df.iterrows():
    tree.insert('', tk.END, values=(row['player_name'], row['age'], row['position'], row['nation'], row['team'], f"$ {row['market_value']} M"))


root.mainloop()
cursor.close()
connection.close()