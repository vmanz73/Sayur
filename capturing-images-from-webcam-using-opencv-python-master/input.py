import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

# the input dialog
USER_INP = simpledialog.askstring(title="Get Class nema",
                                  prompt="Masukan Jenis Sayur:")

# check it out
import os
os.mkdir(USER_INP)