import getpass
import tkinter as tk
from tkinter import ttk
from functions import *

user = getpass.getpass(prompt='User: ')
password = getpass.getpass(prompt='Password: ')

connection = connect_to_database(user, password, "localhost", "player_info")
cursor = connection.cursor()

root = tk.Tk()
root.title("Soccer Player Database")
root.geometry("800x600+100+100")

main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)