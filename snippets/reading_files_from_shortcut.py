'''
import sys
import win32com.client 

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut("t:\\test.lnk")
shortcut.Targetpath = "t:\\ftemp"
shortcut.save()
'''

import pandas as pd
import sys
import win32com.client 
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

shell = win32com.client.Dispatch("WScript.Shell")

shortcut = shell.CreateShortCut(file_path) #'../raw_data/site_visit_beach_well_loc_20180502.xlsx - Shortcut.lnk')

print(shortcut.Targetpath)

file = shortcut.Targetpath

file

df = pd.read_excel(file)

df.head()

